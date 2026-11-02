# Merge two files into a third file

file1 = open("file1.txt", "w")
file1.write("Hello")
file1.close()

file2 = open("file2.txt", "w")
file2.write("Welcome to Python")
file2.close()

file1 = open("file1.txt", "r")
data1 = file1.read()
file1.close()

file2 = open("file2.txt", "r")
data2 = file2.read()
file2.close()

file3 = open("merge.txt", "w")
file3.write(data1 + "\n" + data2)
file3.close()

print("Files merged successfully.")