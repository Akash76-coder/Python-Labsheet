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

# Keep only letters/digits and ignore case so "Madam, I'm Adam" also works
cleaned = ""
for ch in to_lower(text):
    if ch in LOWER or ch in "0123456789":
        cleaned += ch

# Count the length manually
length = 0
for _ in cleaned:
    length += 1

# Compare characters from both ends moving towards the centre
is_palindrome = True
left = 0
right = length - 1
while left < right:
    if cleaned[left] != cleaned[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

if is_palindrome:
    print(f"'{text}' is a Palindrome.")
else:
    print(f"'{text}' is NOT a Palindrome.")