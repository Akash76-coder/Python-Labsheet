paragraph = input("Enter a paragraph: ").lower()

# Replace punctuation with spaces so only words remain
clean = ""
for ch in paragraph:
    clean += ch if ch.isalnum() else " "

freq = {}
for word in clean.split():
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word:<15}{count}")