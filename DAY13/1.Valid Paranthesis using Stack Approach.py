s = input("Enter a string with parentheses: ")
pairs = {')': '(', '}': '{', ']': '['}
stack = []
valid = True
for char in s:
    if char in "({[":  # opening bracket
        stack.append(char)
    elif char in ")}]":  # closing bracket
        if not stack or stack[-1] != pairs[char]:
            valid = False
            break
        stack.pop()
# Final check
if stack:
    valid = False
print("Valid" if valid else "Invalid")