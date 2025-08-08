arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
n = int(input("Enter the number of times to rotate right: "))
length = len(arr)
n = n % length  # to handle n > length
for i in range(n):
    last = arr[-1]
    # shift elements right
    for j in range(length - 1, 0, -1):
        arr[j] = arr[j - 1]
    arr[0] = last
print("After right rotation:", arr)