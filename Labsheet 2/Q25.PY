rows = int(input("Enter number of rows: "))

# Row i prints (rows - i + 1) stars
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()