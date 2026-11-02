text = input("Enter a string: ")

word_count = 0
in_word = False
for ch in text:
    if ch != " ":
        if not in_word:        # a new word starts here
            word_count += 1
            in_word = True
    else:
        in_word = False

print(f"Number of words = {word_count}")