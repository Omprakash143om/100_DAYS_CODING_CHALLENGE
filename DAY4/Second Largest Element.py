arr = list(map(int, input("Enter numbers separated by space: ").split()))
max_element = max(arr)
while max_element in arr:
    arr.remove(max_element)
if len(arr) > 0:
    second_largest = max(arr)
    print("Second Largest:", second_largest)
else:
    print("No second largest element found")
