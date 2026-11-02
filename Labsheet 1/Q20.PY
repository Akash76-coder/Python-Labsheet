# Read marks of 5 subjects (each out of 100)
marks1 = float(input("Enter marks in subject 1: "))
marks2 = float(input("Enter marks in subject 2: "))
marks3 = float(input("Enter marks in subject 3: "))
marks4 = float(input("Enter marks in subject 4: "))
marks5 = float(input("Enter marks in subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
maximum_marks = 5 * 100

# Percentage = (obtained / maximum) x 100
percentage = (total_marks / maximum_marks) * 100

print(f"Total marks obtained = {total_marks} / {maximum_marks}")
print(f"Percentage           = {percentage:.2f}%")