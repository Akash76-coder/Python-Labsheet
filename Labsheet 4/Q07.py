nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

is_sorted = True
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:     # a larger number before a smaller one
        is_sorted = False
        break
print("The list is sorted (ascending)." if is_sorted else "The list is NOT sorted.")