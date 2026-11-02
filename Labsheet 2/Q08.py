main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

# Manual search: compare the substring at every possible starting position
main_length = 0
for _ in main_string:
    main_length += 1
sub_length = 0
for _ in substring:
    sub_length += 1

found = False
start = 0
while start + sub_length <= main_length:
    match = True
    for offset in range(sub_length):
        if main_string[start + offset] != substring[offset]:
            match = False
            break
    if match:
        found = True
        break
    start += 1

if found:
    print(f"'{substring}' is present in '{main_string}' (at index {start}).")
else:
    print(f"'{substring}' is NOT present in '{main_string}'.")