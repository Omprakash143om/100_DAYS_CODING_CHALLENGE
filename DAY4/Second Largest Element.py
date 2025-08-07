arr = list(map(int, input("Enter numbers separated by space: ").split()))
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)