def linearsearch(arr,targetval):
  for i in range(len(arr)):
    if arr[i]==targetval:
      return f"The index value is {i}"
  return -1
arr=list(map(int,input("Enter the numbers with space: ").split()))
targetval=int(input("Enter targetval:"))
print(linearsearch(arr,targetval))