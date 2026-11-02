pairs = ()
for i in range(int(input("How many pairs? "))):
    pairs += ((input(f"Key {i + 1}: "), input(f"Value {i + 1}: ")),)
print("Tuple of tuples:", pairs)
print("Dictionary     :", dict(pairs))