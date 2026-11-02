nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
if not nums:
    print("The list is empty.")
    raise SystemExit

target = int(input("Enter the target sum: "))
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f"Pair: ({nums[i]}, {nums[j]})")
            found = True
if not found:
    print("No pair found.")