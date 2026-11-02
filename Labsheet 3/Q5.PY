text = input("Enter a string: ")

result = ""
for ch in text:
    # Add the character only if it has not been added before
    if ch not in result:
        result += ch

print(f"Original            : {text}")
print(f"After removing dups : {result}")