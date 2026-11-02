t1 = tuple(input("Enter items of first tuple: ").split())
t2 = tuple(input("Enter items of second tuple: ").split())
common = ()
for item in t1:
    if item in t2 and item not in common:
        common += (item,)
print("Common elements:", common if common else "None")