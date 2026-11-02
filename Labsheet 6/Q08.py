
my_set = {10, 20, 30, 40, 50}
element = int(input("Enter element to check: "))
if element in my_set:
  print(f"{element} exists in the set.")
else:
  print(f"{element} does not exist in the set.")