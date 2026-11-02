nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

result = [x for x in nums if x >= 0]
print("List without negatives:", result)