pairs = []
for i in range(int(input("How many tuples? "))):
    pairs.append((input(f"Tuple {i + 1} - first item: "), input(f"Tuple {i + 1} - second item: ")))
print("List of tuples:", pairs)
if pairs:
    first, second = [list(x) for x in zip(*pairs)]       # zip(*) unzips
    print("First list :", first)
    print("Second list:", second)