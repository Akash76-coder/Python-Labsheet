rows = int(input("Enter number of rows: "))

# Row i prints i stars
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()