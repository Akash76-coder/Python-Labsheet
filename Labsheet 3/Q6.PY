text = input("Enter a string: ")

characters = []   # distinct characters (in order of first appearance)
counts = []       # counts[i] is the frequency of characters[i]

for ch in text:
    position = -1
    for i in range(len(characters)):
        if characters[i] == ch:
            position = i
            break
    if position == -1:
        characters.append(ch)
        counts.append(1)
    else:
        counts[position] += 1

print("Character frequencies:")
for i in range(len(characters)):
    shown = "' '(space)" if characters[i] == " " else f"'{characters[i]}'"
    print(f"  {shown} : {counts[i]}")