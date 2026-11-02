side1 = float(input("Enter length of side 1: "))
side2 = float(input("Enter length of side 2: "))
side3 = float(input("Enter length of side 3: "))

# First check that the sides can form a triangle
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Sides must be positive numbers.")
elif side1 + side2 <= side3 or side2 + side3 <= side1 or side1 + side3 <= side2:
    print("These sides cannot form a triangle.")
elif side1 == side2 == side3:
    print("It is an Equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("It is an Isosceles triangle.")
else:
    print("It is a Scalene triangle.")