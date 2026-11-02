t1 = tuple(input("Enter items of first tuple: ").split())
t2 = tuple(input("Enter items of second tuple: ").split())
print("Before swap:", t1, t2)
t1, t2 = t2, t1
print("After swap :", t1, t2)