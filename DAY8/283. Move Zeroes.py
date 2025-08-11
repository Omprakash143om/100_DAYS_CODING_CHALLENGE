nums=list(map(int,input("Enter elements with space:").split()))
slow=-1
for fast in range(0,len(nums)):
    if nums[fast]!=0:
        slow+=1
        nums[slow],nums[fast]=nums[fast],nums[slow]
print(nums) 