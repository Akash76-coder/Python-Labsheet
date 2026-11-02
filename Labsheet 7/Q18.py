# Store unique words in another file

file = open("student.txt", "w")
file.write("apple banana apple mango banana")
file.close()

file = open("student.txt", "r")

words = file.read().split()

file.close()

unique = list(dict.fromkeys(words))

file = open("unique.txt", "w")
file.write(" ".join(unique))
file.close()

print("Unique words saved.")