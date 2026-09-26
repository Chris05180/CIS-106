# Christopher Hernandez  M5P2.py  9/21/26

# Input: Enters the name of item
item_name = str(input("Enter item: "))

# Input: Enters the amount of purchased items
item_quantity = int(input("Enter quantity: "))

# Process: Sets the item price at $10 if item is A
if item_name == "A":
    unit_price = 10
# Process: Sets the item price at $20 if item is B
else:
    item_name = "B"
    unit_price = 20

# Process: Multiplies amount of purchased items by the unit price
extended_price = item_quantity * unit_price

# Output: Displays the item's name, its unit price, and extended price
print(f"You bought {item_name} at ${unit_price:.2f} for "
      f"a total of ${extended_price:.2f}")