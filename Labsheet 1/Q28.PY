character = input("Enter a single character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif "A" <= character <= "Z":
    print(f"'{character}' is an Uppercase letter.")
elif "a" <= character <= "z":
    print(f"'{character}' is a Lowercase letter.")
elif "0" <= character <= "9":
    print(f"'{character}' is a Digit.")
else:
    print(f"'{character}' is a special character.")