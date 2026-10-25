# Christopher Hernandez  M9P1.py  10/19/26

# Process: Setting item total as a float variable
item_total = float()

# Process: Setting extended price as a float variable
extended_price = float()

# Input: Asks user if they want to start program
start_program = str(input("Start program? (Y/N): "))

# Process: Creates a function that determines item total and extended price
def get_extended_price():

# Process: "item_total" is treated as part of the global scope
    global item_total

# Process: Multiplies item amount by item price to get item total
    item_total = item_amount * item_price

# Process: Sets the item discount as .10 in decimal form if item total is greater than $10,000
    if item_total > 10000:
        item_discount = .10

# Process: "extended_price" is treated as part of the global scope
        global extended_price

# Process: Subtracts the product of item total and discount from the item total to get extended price
        extended_price = item_total - (item_total * item_discount)

# Process: Sets the extended price the same as item total
    else:
        extended_price = item_total

# Process: Runs programs while "Y" is entered
while start_program == "Y":

# Input: Enters amount of items
    item_amount = int(input("Enter amount: "))

# Input: Enters price of items
    item_price = float(input("Enter price: "))

# Process: Calls function
    get_extended_price()

# Output: Displays item amount, price of items, and item total
    print(f"{item_amount} items with a price of ${item_price:.2f} "
          f"costs a total of ${item_total:.2f}")

# Output: Displays the item total subtracted from the discount
    print(f"With your discount, the price is ${extended_price:.2f}")

# Input: Asks user if they want to continue program
    start_program = str(input("Do you want to continue? (Y/N): "))
