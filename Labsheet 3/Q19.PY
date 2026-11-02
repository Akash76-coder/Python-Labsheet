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

# Split into words: a word is a run of letters/digits (case ignored, punctuation dropped)
words = []
current = ""
for ch in to_lower(text) + " ":
    if ch in LOWER or ch in "0123456789":
        current += ch
    else:
        if current != "":
            words.append(current)
            current = ""

if len(words) == 0:
    print("No words found.")
else:
    distinct = []
    counts = []
    for word in words:
        position = -1
        for i in range(len(distinct)):
            if distinct[i] == word:
                position = i
                break
        if position == -1:
            distinct.append(word)
            counts.append(1)
        else:
            counts[position] += 1

    best = 0
    for i in range(1, len(distinct)):
        if counts[i] > counts[best]:
            best = i

    print(f"Most repeated word = '{distinct[best]}' (appears {counts[best]} time(s))")