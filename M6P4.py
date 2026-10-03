# Christopher Hernandez  M6P4.py  9/29/26

# Input: Enters amount of tickets bought
quantity_ticket = int(input("Enter amount of tickets: "))

# Process: Determines the ticket price to be an integer value
price_ticket = int()

# Process: Sets the ticket price as $50 if 25 or more tickets were bought
if quantity_ticket >= 25:
    price_ticket = 50
# Process: Sets the ticket price as $100 if tickets bought are between 24 and 10
elif 24 >= quantity_ticket >= 10:
    price_ticket = 100
# Process: Sets the ticket price as $80 if tickets bought are between 9 and 5
elif 9 >= quantity_ticket >= 5:
    price_ticket = 80
# Process: Sets the ticket price as $75 if less than 5 tickets are bought
elif quantity_ticket < 5:
    price_ticket = 75

# Process: Multiplies the ticket's price by the amount of tickets bought
total_cost = price_ticket * quantity_ticket

# Output: Displays the amount of tickets bought, the price per ticket, and the total amount
print(f"You bought {quantity_ticket} tickets at ${price_ticket} "
      f"for a total of ${total_cost:.2f}")