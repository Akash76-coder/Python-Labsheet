text = input("Enter a string: ")

reversed_text = ""
for ch in text:
    # Put each new character in front of the result
    reversed_text = ch + reversed_text

print(f"Original : {text}")
print(f"Reversed : {reversed_text}")