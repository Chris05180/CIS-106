# Christopher Hernandez  M11P5.py  11/6/26

# Process: Sets item total as float variable
item_total = float()

# Process: Sets item tax as float variable
item_tax = float()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (Y/N): "))

# Process: Creates function that determines item total and item tax
def get_total_and_tax():

# Process: "item_total" is treated as global variable
    global item_total

# Process: Multiplies item quantity and item price to get item total
    item_total = item_quanty * item_price

# Process: "item_tax" is treated as global variable
    global item_tax

# Process: Multiplies item total by 7%
    item_tax = item_total * .07

# Process: Runs program while "Y" is entered
while program_start == "Y":

# Input: Asks for quantity of the item
    item_quanty = int(input("Enter quantity of item: "))

# Input: Asks for price of the item
    item_price = float(input("Enter price of item: "))

# Process: Calls the function
    get_total_and_tax()

# Output: Displays item total and item tax
    print(f"Your total is ${item_total:.2f} with tax of ${item_tax:.2f}")

# Input: Asks user if they want to run the program again
    program_start = str(input("Run again? (Y/N): "))