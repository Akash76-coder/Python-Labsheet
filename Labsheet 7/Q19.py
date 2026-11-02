# Sort words alphabetically

file = open("student.txt", "w")
file.write("mango apple banana")
file.close()

file = open("student.txt", "r")

words = file.read().split()

file.close()

words.sort()

file = open("sorted.txt", "w")
file.write(" ".join(words))
file.close()

print("Words sorted successfully.")