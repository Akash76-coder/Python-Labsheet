text = input("Enter a string: ")

length = 0
for _ in text:
    length += 1

print(f"All substrings of '{text}':")
count = 0
# i = start index, j = end index (exclusive)
for i in range(length):
    for j in range(i + 1, length + 1):
        print(text[i:j])
        count += 1

print(f"Total substrings = {count}")