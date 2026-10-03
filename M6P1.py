# Christopher Hernandez  M6P1.py  9/28/2026

# Input: Enters amount of widgets
quantity_widget = int(input("Enter amount: "))

# Process: Sets the initial price at $10 if amount of widgets is above 10,000
if quantity_widget > 10000:
    initial_price = 10
# Process: Sets the initial price at $20 if amount of widgets is between 10,000 and 5,000
if 10000 >= quantity_widget >= 5000:
    initial_price = 20
# Process: Sets the initial price at $30 if amount of widgets is different
else:
    initial_price = 30

# Process: Multiplies the amount of widgets by their initial price
extended_price = quantity_widget * initial_price

# Process: Multiplies the extended price by 7%
tax_amount = extended_price * .07

# Process: Adds the extended price and the tax
total_amount = extended_price + tax_amount

# Output: Display the extended price, tax, and total amount spent
print(f"You must pay ${extended_price:.2f} with a ${tax_amount:.2f} tax "
      f"for a total of ${total_amount:.2f}")
