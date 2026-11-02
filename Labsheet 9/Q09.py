# Save and read student data

file = open("students.txt", "w")

file.write("1,Akash,85\n")
file.write("2,Rahul,90\n")
file.write("3,Mohit,75\n")

file.close()

print("Student data saved successfully.")

# Read student data
file = open("students.txt", "r")

print("Student Records:")

for line in file:
    print(line.strip())

file.close()