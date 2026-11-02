items = input("Enter list items separated by spaces: ").split()
text = ""
for i in range(len(items)):
    text += items[i]
    if i < len(items) - 1:
        text += " "
print("List  :", items)
print("String:", text)