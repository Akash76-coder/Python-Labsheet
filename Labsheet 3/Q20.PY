first = input("Enter first string: ")
second = input("Enter second string: ")

# Two strings are rotations if they have equal length and the second
# string appears inside (first + first)
if len(first) != len(second):
    print("The strings are NOT rotations of each other (different lengths).")
else:
    doubled = first + first
    found = False
    for start in range(len(doubled) - len(second) + 1):
        match = True
        for k in range(len(second)):
            if doubled[start + k] != second[k]:
                match = False
                break
        if match:
            found = True
            break

    if found:
        print(f"'{second}' is a rotation of '{first}'.")
    else:
        print("The strings are NOT rotations of each other.")