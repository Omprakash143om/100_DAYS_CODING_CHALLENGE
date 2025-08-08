arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
i = int(input("Enter the positive index of the element to delete: "))
# Shift elements to the left from index i
for j in range(i, len(arr) - 1):
    arr[j] = arr[j + 1]
# Reduce list size by 1 manually
arr = arr[:-1]
print("After deletion:", arr)
