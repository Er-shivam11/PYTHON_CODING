# Input: prices = [7,1,5,3,6,4]
# Output: 5
# def stocksell(price):
prices = [7, 1, 5, 3, 6, 4]
min_price = float('inf')
max_profit=0
for price in prices:
    if price < min_price:
        min_price = price
    elif price - min_price > max_profit:
        max_profit=price-min_price
print(max_profit)


# print(min_price)
