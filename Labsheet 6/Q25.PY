
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
common_letters = set(str1) & set(str2)
print("Common letters:", common_letters)