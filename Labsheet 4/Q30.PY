text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1      # get() returns 0 for a new character
print("Dictionary:", freq)