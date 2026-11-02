main_string = input("Enter the main string: ")
substring = input("Enter the substring to search: ")

main_length = 0
for _ in main_string:
    main_length += 1
sub_length = 0
for _ in substring:
    sub_length += 1

# Compare the substring at every possible starting position
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
    print(f"'{substring}' EXISTS in '{main_string}' (first found at index {start}).")
else:
    print(f"'{substring}' does NOT exist in '{main_string}'.")