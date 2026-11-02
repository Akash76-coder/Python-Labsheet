# Convert file content into uppercase

file = open("student.txt", "r")

data = file.read()

print(data.upper())

file.close()