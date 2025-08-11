nums = list(map(int, input("Enter elements with space: ").split()))
if not nums:
    print(0)
# Index for placing unique elements
k = 1
for i in range(1, len(nums)):
    if nums[i] != nums[k - 1]:
        nums[k] = nums[i]
        k += 1
print(k)