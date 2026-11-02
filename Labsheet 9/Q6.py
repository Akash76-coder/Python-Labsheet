# CRUD operations using dictionary

employees = {
    1: {"name": "Akash", "salary": 25000},
    2: {"name": "Rahul", "salary": 30000}
}

# Create
employees[3] = {"name": "Mohit", "salary": 28000}

print("After Adding:", employees)

# Read
print("Employee:", employees[1])

# Update
employees[1]["salary"] = 35000

print("After Updating:", employees)

# Delete
del employees[2]

print("After Deleting:", employees)