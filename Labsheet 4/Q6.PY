nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

mid = (len(nums) + 1) // 2      # first half gets the extra element if length is odd
print("First half :", nums[:mid])
print("Second half:", nums[mid:])