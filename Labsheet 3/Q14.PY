text = input("Enter a string: ")

PUNCTUATION = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

result = ""
for ch in text:
    if ch not in PUNCTUATION:
        result += ch

print(f"Original         : {text}")
print(f"Without punctuation : {result}")