t = tuple(input("Enter items separated by spaces: ").split())
if not t:
    raise SystemExit("The tuple is empty.")

text = ""
for item in t:
    text += item + " "
print("Tuple :", t)
print("String:", text.strip())