text = input("Enter a string: ")

vowels = 0
consonants = 0
for ch in text:
    if ch in "aeiouAEIOU":
        vowels += 1
    elif ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        consonants += 1   # alphabet but not a vowel

print(f"Vowels     : {vowels}")
print(f"Consonants : {consonants}")