text = input("Enter a string: ")

first_unique = None
for i in range(len(text)):
    repeated = False
    for j in range(len(text)):
        if i != j and text[i] == text[j]:
            repeated = True
            break
    if not repeated:
        first_unique = text[i]
        break

if first_unique is None:
    print("There is no non-repeated character.")
else:
    print(f"First non-repeated character = '{first_unique}'")