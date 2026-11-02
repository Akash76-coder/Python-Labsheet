text = input("Enter a string: ")

uppercase_chars = ""
for ch in text:
    if "A" <= ch <= "Z":
        uppercase_chars += ch

if uppercase_chars == "":
    print("No uppercase characters found.")
else:
    print(f"Uppercase characters: {uppercase_chars}")