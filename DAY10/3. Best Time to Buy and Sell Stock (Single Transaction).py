# Best Time to Buy and Sell Stock
prices = list(map(int, input("Enter stock prices separated by space: ").split()))
min_price = float('inf')
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit = price - min_price
print("Maximum profit:", max_profit)
