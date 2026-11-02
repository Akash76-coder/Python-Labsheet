# Remove blank lines

file = open("student.txt", "w")
file.write("Hello\n\nPython\n\nWelcome")
file.close()

file = open("student.txt", "r")

lines = file.readlines()

file.close()

file = open("student.txt", "w")

for line in lines:
    if line.strip():
        file.write(line)

file.close()

print("Blank lines removed.")