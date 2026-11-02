text = input("Enter a string: ")

characters = list(text)
n = len(characters)

# Bubble sort: repeatedly swap neighbouring characters that are out of order
for i in range(n - 1):
    for j in range(n - 1 - i):
        if characters[j] > characters[j + 1]:
            characters[j], characters[j + 1] = characters[j + 1], characters[j]

sorted_text = ""
for ch in characters:
    sorted_text += ch

print(f"Original : {text}")
print(f"Sorted   : {sorted_text}")