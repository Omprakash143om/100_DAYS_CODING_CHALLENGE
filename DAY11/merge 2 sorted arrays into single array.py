# Merge two sorted lists using Two Pointers
# Input: First sorted list
arr1 = list(map(int, input("Enter the first sorted list elements separated by space: ").split()))
# Input: Second sorted list
arr2 = list(map(int, input("Enter the second sorted list elements separated by space: ").split()))
# Two pointers
i = 0
j = 0
merged = []
# Compare elements and merge
while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1
# Add remaining elements (if any)
while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1
# Output merged list
print("Merged Sorted List:", merged)