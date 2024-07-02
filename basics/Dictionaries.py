# Creating a dictionary
student = {
    "name": "Faizan",
    "age": 22,
    "courses": ["Software Testing", "Artificial Intelligence"]
}

print("---------------------------------------------------")
print("---------------------------------------------------")

# 1. Accessing elements
print("Name:", student["name"])
print("Age", student["age"])
print("Courses:", student["courses"])

print("---------------------------------------------------")
print("---------------------------------------------------")

# 2. Adding a new key-value pair
student["grade"] = "B"
print("After adding grade: ", student)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 3. Updating an existing key-value pair
student["age"] = 23
print("After updating age:", student)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 4. Removing a key-value pair
del student["grade"]
print("After removing grade:", student)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 5. Using the pop method to remove a key-value pair and get its value
courses = student.pop("courses")
print("After popping courses: ", student)
print("Popped courses: ", courses)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 6. Checking if a key exists in the dictionary
has_name = "name" in student
print("Does the dictionary have a 'name' key: ", has_name)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 7. Adding the courser back to the dict
student["courses"] = courses
print("After adding courses to the dict: ", student)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 8. Iterating through the dict
for key, value in student.items():
    print(f"{key}: {value}")

print("---------------------------------------------------")
print("---------------------------------------------------")

# 8. Getting all keys
keys = student.keys()
print("Keys:", keys)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 9. Getting all values
values = student.values()
print("Values:", values)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 10. Getting all key-value pairs
items = student.items()
print("Items:", items)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 11. Using the get method to safely access values
age = student.get("age")
print("Age:", age)

print("---------------------------------------------------")
print("---------------------------------------------------")

# 12. Using the get method with a default value
grade = student.get("grade", "N/A")
print("Grade:", grade)
