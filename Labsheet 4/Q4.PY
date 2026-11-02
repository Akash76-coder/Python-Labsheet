nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

product = 1
for x in nums:
    product *= x
print("Product =", product)