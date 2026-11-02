# Write multiple lines into a file

file = open("student.txt", "w")

for i in range(3):
    data = input("Enter a line: ")
    file.write(data + "\n")

file.close()

print("Data saved successfully.")