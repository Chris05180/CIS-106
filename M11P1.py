# Christopher Hernandez  M11P1.py  11/4/26

# Process: Sets discounted price as float variable
discount_price = float()

# Process: Sets discounted amount as float variable
discount_amount = float()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (Y/N): "))

# Process: Creates a function that determines discount amount and price
def get_discount_amount_price():

# Process: "discount_amount" is treated as global variable
    global discount_amount

# Process: Multiplies item price and discount rate to get discount amount
    discount_amount = item_price * discount_rate

# Process: "discount_price" is treated as global variable
    global discount_price

# Process: Subtracts discount amount from item price
    discount_price = item_price - discount_amount

# Process: Runs program while "Y" is entered
while program_start == "Y":

# Input: Asks user for the item quantity
    item_quantity = int(input("Enter quantity: "))

# Input: Asks user for the item price
    item_price = float(input("Enter price: "))

# Input: Asks user for the discount rate
    discount_rate = float(input("Enter discount rate: "))

# Process: Calls the function
    get_discount_amount_price()

# Output: Displays the item quantity and item prices
    print(f"{item_quantity} items cost ${item_price:.2f} ")

# Output: Displays the discount price and discounted amount
    print(f"With your discount the items now cost ${discount_price:.2f}"
          f"\nYou saved ${discount_amount:.2f}!")

# Input: Asks user if they want to run the program again
    program_start = str(input("Run again? (Y/N): "))

