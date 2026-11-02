rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Leading spaces to centre the pyramid
    for _ in range(rows - i):
        print(" ", end=" ")
    # Print 1 up to i, then back down to 1
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()