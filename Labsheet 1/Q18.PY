# Read weight (kg) and height (m)
weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

if height <= 0:
    print("Error: Height must be greater than zero.")
else:
    # BMI = weight / (height x height)
    bmi = weight / (height * height)
    print(f"Your BMI = {bmi:.2f}")

    # Classify using standard BMI ranges
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")