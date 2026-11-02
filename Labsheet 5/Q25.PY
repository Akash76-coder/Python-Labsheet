t1 = tuple(input("Enter items of first tuple: ").split())
t2 = tuple(input("Enter items of second tuple: ").split())
print("t1 - t2:", tuple(x for x in t1 if x not in t2))
print("t2 - t1:", tuple(x for x in t2 if x not in t1))