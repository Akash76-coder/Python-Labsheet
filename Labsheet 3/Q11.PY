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


first = to_lower(input("Enter first string: "))
second = to_lower(input("Enter second string: "))

# Ignore spaces; count how many letters each string has
def clean(text):
    result = ""
    for ch in text:
        if ch != " ":
            result += ch
    return result

first = clean(first)
second = clean(second)

# Anagrams: same characters with the same counts
remaining = list(second)
is_anagram = True
for ch in first:
    found = False
    for i in range(len(remaining)):
        if remaining[i] == ch:
            remaining.pop(i)     # use up this character
            found = True
            break
    if not found:
        is_anagram = False
        break

if is_anagram and len(remaining) == 0:
    print("The strings are Anagrams.")
else:
    print("The strings are NOT Anagrams.")