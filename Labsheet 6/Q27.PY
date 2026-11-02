
str1 = input("Enter first string: ").strip()
str2 = input("Enter second string: ").strip()
if set(str1) == set(str2) and len(str1) == len(str2):
  print("The strings are anagrams.")
else:
  print("The strings are not anagrams.")