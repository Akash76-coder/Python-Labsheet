# Count occurrence of a word

file = open("student.txt", "r")

data = file.read()

word = input("Enter word: ")

count = data.split().count(word)

print("Word count:", count)

file.close()