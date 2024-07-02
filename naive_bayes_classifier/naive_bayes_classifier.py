import pandas as pd
from collections import defaultdict

# Define the dataset
data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'],
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny',
                'Overcast', 'Overcast', 'Rain'],
    'Temp.': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot',
              'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
             'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Convert dataset to DataFrame
df = pd.DataFrame(data)


# Function to calculate probabilities
def calculate_probabilities(df):
    total_instances = len(df)
    decision_counts = df['Decision'].value_counts()
    prior_prob_yes = decision_counts['Yes'] / total_instances
    prior_prob_no = decision_counts['No'] / total_instances

    conditional_probs = defaultdict(dict)
    for column in df.columns[1:-1]:  # Exclude 'Day' and 'Decision' columns
        for value in df[column].unique():
            for decision in df['Decision'].unique():
                count = len(df[(df[column] == value) & (df['Decision'] == decision)])
                total_decision_count = decision_counts[decision]
                conditional_probs[column][(value, decision)] = count / total_decision_count

    return prior_prob_yes, prior_prob_no, conditional_probs


# Function to predict decision for new instance
def predict_decision(instance, prior_prob_yes, prior_prob_no, conditional_probs):
    prob_yes = prior_prob_yes
    prob_no = prior_prob_no
    for attr, value in instance.items():
        if attr != 'Decision':
            prob_yes *= conditional_probs[attr].get((value, 'Yes'), 0)
            prob_no *= conditional_probs[attr].get((value, 'No'), 0)
    return 'Yes' if prob_yes > prob_no else 'No'


# Calculate probabilities
prior_prob_yes, prior_prob_no, conditional_probs = calculate_probabilities(df)

# Test with a new instance
new_instance = {'Outlook': 'Sunny', 'Temp.': 'Cool', 'Humidity': 'High', 'Wind': 'Strong'}
predicted_decision = predict_decision(new_instance, prior_prob_yes, prior_prob_no, conditional_probs)
print("Predicted decision for the new instance:", predicted_decision)
