arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
n = int(input("Enter the number of times to rotate left: "))
length = len(arr)
n = n % length  # to handle n > length
for i in range(n):
    first = arr[0]
    # shift elements left
    for j in range(0, length - 1):
        arr[j] = arr[j + 1]
    arr[-1] = first
print("After left rotation:", arr)
