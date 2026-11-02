UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


def to_lower(text):
    """Convert text to lowercase without using lower()."""
    result = ""
    for ch in text:
        converted = ch
        for i in range(26):
            if ch == UPPER[i]:
                converted = LOWER[i]
        result += converted
    return result


def to_upper(text):
    """Convert text to uppercase without using upper()."""
    result = ""
    for ch in text:
        converted = ch
        for i in range(26):
            if ch == LOWER[i]:
                converted = UPPER[i]
        result += converted
    return result


text = input("Enter a string: ")

result = ""
for ch in text:
    if ch in "aeiouAEIOU":
        result += to_upper(ch)      # vowel -> uppercase
    elif ch in UPPER or ch in LOWER:
        result += to_lower(ch)      # consonant -> lowercase
    else:
        result += ch                # digits, spaces, symbols unchanged

print(f"Original : {text}")
print(f"Modified : {result}")