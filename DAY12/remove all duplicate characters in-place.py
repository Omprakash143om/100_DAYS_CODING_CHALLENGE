# Take input string and convert to list of chars
chars = list(input("Enter string: "))
# Two pointers
i = 0  # Index for placing unique chars
for j in range(len(chars)):
    # Check if chars[j] is already in the range 0 to i-1
    if chars[j] not in chars[:i]:
        chars[i] = chars[j]  # Place unique char
        i += 1  # Move unique placement pointer
# Slice the list to remove unwanted chars after i
chars = chars[:i]
# Convert back to string and display
print("After removing duplicates:", "".join(chars))
