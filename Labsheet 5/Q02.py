name = input("Enter name (str): ")
age = int(input("Enter age (int): "))
height = float(input("Enter height in metres (float): "))
is_student = input("Is a student? (yes/no): ").lower() == "yes"    # bool

person = (name, age, height, is_student)
print("Tuple:", person)
for item in person:
    print(f"{str(item):<10} -> {type(item).__name__}")