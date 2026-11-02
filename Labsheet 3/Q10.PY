text = input("Enter a string: ")

longest_word = ""
longest_length = 0
current_word = ""
current_length = 0

for ch in text + " ":
    if ch != " ":
        current_word += ch
        current_length += 1
    else:
        if current_length > longest_length:
            longest_word = current_word
            longest_length = current_length
        current_word = ""
        current_length = 0

if longest_length == 0:
    print("No words found.")
else:
    print(f"Longest word = '{longest_word}' ({longest_length} characters)")