# Christopher Hernandez  M4P2.py  9/15/2026

# Input: Types in purchase price per share
price_per_share = float(input("Type in purchase price per share: $"))

# Input: Types in current stock price
current_price = float(input("Type in current stock price: $"))

# Input: Types in quantity of stock
stock_quantity = int(input("Type in stock quantity: "))

# Process: Multiplies stock quantity by the difference between the current stock price and purchase price per share
stock_value = (current_price - price_per_share) * stock_quantity

# Output: Displays the stock value
print(f"Your value is ${stock_value:.2f}")

if stock_value > 0:
    print("You are gaining money!")
else:
    print("You are losing money!")