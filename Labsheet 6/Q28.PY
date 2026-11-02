
fs = frozenset([1, 2, 3, 4])
print("Frozenset:", fs)
print("Type:", type(fs))

try:
  fs.add(5)
except AttributeError as e:
  print("Error caught on modification attempt:", e)