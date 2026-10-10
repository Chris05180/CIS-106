# Christopher Hernandez  M7P5.py  10/6/26

# Input: Enters YES to start program or NO to not start it
program_start = str(input("Start program? YES/NO: "))

# Process: Sets the sum of all discounts to 0
sum_discount = 0

# Process: Starts the program while YES is entered
while program_start == "YES":
# Input: Enters the amount of items bought
    item_quantity = int(input("Enter quantity of item: "))
# Input: Enters the price of items bought
    item_price = float(input("Enter price of item: "))
# Process: Multiplies the item's quantity by its price
    extended_price = item_quantity * item_price
# Process: If the extended price is above $10,000 the discount is set at 25% otherwise it's set at 10%
    if extended_price > 10000:
        item_discount = .25
    else: item_discount = .10
# Process: Multiplies the item's extended price by the item's discount
    discount_amount = extended_price * item_discount
# Process: Sums up the discount amounts for each discount amount entered
    sum_discount += discount_amount
# Process: Subtracts the discount amount from the item's extended price
    total_price = extended_price - discount_amount
# Output: Displays the item's discount amount, extended price, and total price
    print(f"With a ${discount_amount:.2f} discount, your "
          f"${extended_price:.2f} purchase is now ${total_price:.2f}")
# Input: Asks user if they want to continue program through a YES or NO
    program_start = str(input("Continue program? YES/NO: "))

# Output: Displays the sum of all discounts
print(f"The sum of all discount is ${sum_discount:.2f}")