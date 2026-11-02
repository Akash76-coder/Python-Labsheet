# Replace a word in a file

file = open("student.txt", "w")
file.write("I am learning Python.")
file.close()

file = open("student.txt", "r")
data = file.read()
file.close()

data = data.replace("Python", "Java")

file = open("student.txt", "w")
file.write(data)
file.close()

print("Word replaced successfully.")