# Display even-numbered lines

file = open("student.txt", "r")

for i, line in enumerate(file, start=1):
    if i % 2 == 0:
        print(line)

file.close()