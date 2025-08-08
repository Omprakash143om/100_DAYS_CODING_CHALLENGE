arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
y = int(input("Enter the index at which to insert the new element: "))
x = int(input("Enter the element to insert: "))
# Increase list size by 1 manually
arr = arr + [0]
# Shift elements to the right
for i in range(len(arr) - 1, y, -1):
    arr[i] = arr[i - 1]
# Insert x at position y
arr[y] = x
print("After insertion:", arr)
