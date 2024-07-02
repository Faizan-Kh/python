import numpy as np

# Generating fictional sensor data
np.random.seed(0)
sensor1 = np.random.rand(5)  # Sensor 1 data (fictional)
sensor2 = np.random.rand(5)  # Sensor 2 data (fictional)
membership_values = ['Low', 'Medium', 'High', 'Very High', 'Extreme']

# Task #1: Union according to the Gain value of sensor1 and sensor2 detection values.
union_sensor = [max(s1, s2) for s1, s2 in zip(sensor1, sensor2)]
print("Union according to Gain value:")
print(dict(zip(membership_values, union_sensor)))

# Task #2: Intersection according to the Gain value of sensor1 and sensor2 detection values.
intersection_sensor = [min(s1, s2) for s1, s2 in zip(sensor1, sensor2)]
print("\nIntersection according to Gain value:")
print(dict(zip(membership_values, intersection_sensor)))

# Task #3: Difference according to the Gain value of sensor1 and sensor2 detection values.
difference_sensor = [abs(s1 - s2) for s1, s2 in zip(sensor1, sensor2)]
print("\nDifference according to Gain value:")
print(dict(zip(membership_values, difference_sensor)))

# Task #4: Complement of Sensor 1 and Sensor 2
complement_sensor1 = [1 - d for d in sensor1]
complement_sensor2 = [1 - d for d in sensor2]
print("\nComplement of Sensor 1:")
print(dict(zip(membership_values, complement_sensor1)))
print("\nComplement of Sensor 2:")
print(dict(zip(membership_values, complement_sensor2)))

# Task #5: Min-Max Composition of sets A and B
A = np.array([[0.6, 0.3], [0.2, 0.9]])
B = np.array([[1, 0.5, 0.3], [0.8, 0.4, 0.7]])
max_min_composition = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        min_values = [min(A[i, k], B[k, j]) for k in range(A.shape[1])]
        max_min_composition[i, j] = max(min_values)

print("\nMax-Min Composition:")
print(max_min_composition)

# Task #6: Max-Product Composition of sets A and B
max_product_composition = np.zeros((A.shape[0], B.shape[1]))

for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        product_values = [A[i, k] * B[k, j] for k in range(A.shape[1])]
        max_product_composition[i, j] = max(product_values)

print("\nMax-Product Composition:")
print(max_product_composition)
