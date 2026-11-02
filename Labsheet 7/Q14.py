# Find the longest line

file = open("student.txt", "r")

lines = file.readlines()

longest = max(lines, key=len)

print("Longest line:", longest)

file.close()