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
new_word = True   # True when the next character starts a word
for ch in text:
    if ch == " ":
        result += ch
        new_word = True
    elif new_word:
        result += to_upper(ch)   # first letter of a word -> uppercase
        new_word = False
    else:
        result += to_lower(ch)   # remaining letters -> lowercase

print(f"Original   : {text}")
print(f"Title case : {result}")