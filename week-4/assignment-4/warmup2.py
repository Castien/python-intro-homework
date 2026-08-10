

# Create a hardcoded dictionary representing a student with these keys: 
# name, grade, and subjects (a list of subject strings). 
# Then:
# Print each key-value pair using .items() in a for loop
# Add a new key "graduated" with the value False
# Print the updated dictionary

student = {
    "name": "Pikachu",
    "grade": 95,
    "subjects": ["Thunderbolt", "Quick Attack", "Iron Tail"]
}

# Print each key-value pair using .items()
for key, value in student.items():
    print(f"{key}: {value}")

# Add graduated key
student["graduated"] = False

# Print updated dictionary
print(student)