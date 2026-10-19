# Christopher Hernandez  10/15/26  M8P4.py

# Process: Sets the total extended price to be a float value
total_extended_price = float()

# Process: Sets the order counter to 0
order_counter = 0

# Process: Opens and closes text file to read it
with open('M8P4FILE.txt', 'r') as f:
# Process: While true, reads one line and removes blank line
    while 1==1:
        item_name = f.readline().strip()
# Process: Terminates closest enclosing loop
        if not item_name:
            break
# Process: Reads one line, turns it into integer value, and removes blank line
        item_quantity = int(f.readline().strip())
# Process: Reads one line, turns it into float value, and removes blank line
        item_price = float(f.readline().strip())
# Process: Multiplies amount of items by their price to get extended price
        extended_price = item_quantity * item_price
# Output: Displays the item, quantity, price, and extended price
        print(f"{item_name}: {item_quantity} at ${item_price} for"
              f" ${extended_price}")
# Process: Sums up each previous extended price
        total_extended_price += extended_price
# Process: Adds one to the previous order counter
        order_counter += 1

# Process: Divides the total extended price by the order counter to get the average order
average_order = total_extended_price/order_counter

# Output: Displays total extended price, amount of orders, and the average counter
print(f"The total extended price is ${total_extended_price}, "
      f"there are {order_counter} orders, and the average "
      f"order is ${average_order}")



