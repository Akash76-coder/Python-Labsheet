nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

total = 0
for x in nums:
    total += x
print(f"Sum = {total}, Average = {total / len(nums):.2f}")