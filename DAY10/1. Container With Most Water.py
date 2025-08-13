# Container With Most Water
heights = list(map(int, input("Enter heights separated by space: ").split()))
left = 0
right = len(heights) - 1
max_area = 0
while left < right:
    # Calculate area between left and right
    height = min(heights[left], heights[right])
    width = right - left
    area = height * width
    max_area = max(max_area, area)
    # Move the pointer with smaller height
    if heights[left] < heights[right]:
        left += 1
    else:
        right -= 1

print("Maximum water area:", max_area)
