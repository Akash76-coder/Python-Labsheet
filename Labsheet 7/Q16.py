# Display first and last lines

file = open("student.txt", "r")

lines = file.readlines()

if lines:
    print("First line:", lines[0].strip())
    print("Last line:", lines[-1].strip())
else:
    print("File is empty.")

file.close()