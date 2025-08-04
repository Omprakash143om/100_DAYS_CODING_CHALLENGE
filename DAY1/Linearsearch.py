def binarysearch(arr,targetval):
  arr.sort()
  print(arr)
  left=0
  right=len(arr)
  while left<=right:
    mid=(left+right)//2
    if arr[mid]==targetval:
      return f"The index value is {mid}"
    elif arr[mid]<targetval:
      left=mid+1
    else:
      right=mid-1
  return -1
arr=list(map(int,input("Enter the numbers with space: ").split()))
targetval=int(input("Enter targetval:"))
print(binarysearch(arr,targetval))