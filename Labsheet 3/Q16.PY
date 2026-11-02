text = input("Enter a string: ")

digits = 0
alphabets = 0
special = 0
for ch in text:
    if "0" <= ch <= "9":
        digits += 1
    elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        alphabets += 1
    else:
        special += 1     # spaces and symbols are counted as special

print(f"Digits             : {digits}")
print(f"Alphabets          : {alphabets}")
print(f"Special characters : {special}")