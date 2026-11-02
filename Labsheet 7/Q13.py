# Read numbers from a file

file = open("numbers.txt", "w")
file.write("10 20 30 40 50")
file.close()

file = open("numbers.txt", "r")

numbers = list(map(int, file.read().split()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

file.close()s