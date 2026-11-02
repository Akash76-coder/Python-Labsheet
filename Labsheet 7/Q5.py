# Count lines and characters

file = open("student.txt", "r")

data = file.read()

lines = data.splitlines()

print("Total lines:", len(lines))
print("Total characters:", len(data))

file.close()