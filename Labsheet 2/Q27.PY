# Nested loops: outer loop = row (multiplier), inner loop = column (table)
print("Multiplication Table (1 to 10)")
print()
for row in range(1, 11):
    for column in range(1, 11):
        print(f"{row * column:4d}", end="")
    print()