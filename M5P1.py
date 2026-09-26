# Christopher Hernandez  M5P1.py  9/21/26

# Input: Enters the amount of item purchased
item_quantity = int(input("Enter quantity of item: "))

# Process: Sets the item price as $3 if 1000 or more items are bought
if item_quantity >= 1000:
    unit_price = 3
    print(f"Item is ${unit_price:.2f}")
# Process: Sets the item price as $5 if less than 1000 items are bought
else:
    unit_price = 5
    print(f"Item is ${unit_price:.2f}")

# Process: Multiplies the amount of the item by the price of the item
extended_price = item_quantity * unit_price

# Process: Multiplies the extended price of item by a 7% tax
item_tax = extended_price * .07

# Process: Adds the item's extended price and the item's tax
item_total = extended_price + item_tax

# Output: Displays the amount of item, its unit price, and extended price
print(f"You bought {item_quantity} items at ${unit_price:.2f} "
      f"each for a total of ${extended_price:.2f} without tax")

# Output: Displays the item's total and its tax
print(f"With tax your total is ${item_total:.2f} with a ${item_tax:.2f} tax")
