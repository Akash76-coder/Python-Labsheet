angle1 = float(input("Enter first angle (degrees): "))
angle2 = float(input("Enter second angle (degrees): "))
angle3 = float(input("Enter third angle (degrees): "))

# Valid triangle: every angle > 0 and the angles add up to 180
if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 + angle2 + angle3 == 180:
    print("The triangle is VALID.")
else:
    print("The triangle is NOT valid.")