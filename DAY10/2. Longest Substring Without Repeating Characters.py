# Longest Substring Without Repeating Characters
s = input("Enter a string: ")
char_set = set()
left = 0
max_length = 0
for right in range(len(s)):
    # Shrink window if duplicate found
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    char_set.add(s[right])
    max_length = max(max_length, right - left + 1)
print("Length of longest substring without repetition:", max_length)