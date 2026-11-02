nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

n = int(input("Rotate left by n positions: ")) % len(nums)
print("Rotated list:", nums[n:] + nums[:n])