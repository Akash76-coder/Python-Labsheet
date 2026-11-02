character = input("Enter a single character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif ("a" <= character <= "z") or ("A" <= character <= "Z"):
    # It is an alphabet; check if it is one of the vowels
    if character in "aeiouAEIOU":
        print(f"'{character}' is a Vowel.")
    else:
        print(f"'{character}' is a Consonant.")
else:
    print(f"'{character}' is not an alphabet.")