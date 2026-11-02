marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter a value between 0 and 100.")
elif marks >= 90:
    print(f"Marks: {marks} -> Grade: A")
elif marks >= 75:
    print(f"Marks: {marks} -> Grade: B")
elif marks >= 50:
    print(f"Marks: {marks} -> Grade: C")
else:
    print(f"Marks: {marks} -> Grade: F")