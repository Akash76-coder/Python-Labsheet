# Copy one file into another

file1 = open("student.txt", "r")
data = file1.read()
file1.close()

file2 = open("copy.txt", "w")
file2.write(data)
file2.close()

print("File copied successfully.")