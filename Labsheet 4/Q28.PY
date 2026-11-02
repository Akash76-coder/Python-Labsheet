students = {}
for _ in range(int(input("How many students? "))):
    roll = input("Roll number: ")
    students[roll] = {"Name": input("Name: "), "Roll": roll, "Marks": float(input("Marks: "))}

print("\nStudent Details")
for roll, info in students.items():
    print(f"{roll}: Name = {info['Name']}, Roll = {info['Roll']}, Marks = {info['Marks']}")