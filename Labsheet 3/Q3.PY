text = input("Enter a string: ")

result = ""
for ch in text:
    if ch == " ":
        result += "_"
    else:
        result += ch

print(f"Original : {text}")
print(f"Modified : {result}")