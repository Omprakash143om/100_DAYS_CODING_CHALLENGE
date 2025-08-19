def climbStairs(n):
    if n <= 2:
        return n
    
    first, second = 1, 2  # ways to reach step 1 and step 2
    for i in range(3, n + 1):
        third = first + second
        first, second = second, third
    return second

# 🔹 Sample Input/Output
n = int(input("Enter number of steps: "))
print("Number of distinct ways:", climbStairs(n))
