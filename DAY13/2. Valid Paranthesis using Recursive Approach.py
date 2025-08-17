def is_valid_recursive(s):
    if s == "":
        return True
    new_s = s.replace("()", "").replace("{}", "").replace("[]", "")
    if new_s == s:  # no change → invalid
        return False
    return is_valid_recursive(new_s)
# User input
s = input("Enter a string with parentheses: ")
print("Valid" if is_valid_recursive(s) else "Invalid")
