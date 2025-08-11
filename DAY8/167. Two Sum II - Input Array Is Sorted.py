numbers = list(map(int,input("Enter sorted elements with space:").split()))
target = int(input("Enter target value:"))
left = 0
right = len(numbers) - 1
while left < right:
    current_sum = numbers[left] + numbers[right]
    if current_sum == target:
        print([left + 1, right + 1])  # 1-based index
        break  # Stop after finding the pair
    elif current_sum < target:
        left += 1
    else:
        right -= 1