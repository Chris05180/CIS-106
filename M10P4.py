# Christopher Hernandez  M10P4.py  10/28/26

# Process: Sets the sum ticket price counter to 0
sum_ticket_price = 0

# Process: Sets the ticket price as an integer value
ticket_price = int()

# Input: Asks user if they want to start program
run_program = str(input("Run program? (y/n): "))

# Process: Creates function to determine train ticket price
def get_train_ticket_price():

# Process: "ticket_price" is treated as a global
    global ticket_price

# Process: Sets the ticket price at $12 if distance from Chicago is 30 miles
    if distance_chicago >= 30:
        ticket_price = 12

# Process: Sets the ticket price at $10 if distance from Chicago is between 20 and 29 miles
    elif 20 <= distance_chicago <= 29:
        ticket_price = 10

# Process: Sets the ticket price at $8 if distance from Chicago is between 10 and 19 miles
    elif 10 <= distance_chicago <= 19:
        ticket_price = 8

# Process: Sets the ticket price at $5 if distance from Chicago is anything else
    else:
        ticket_price = 5

# Process: Continues the program while "y" is entered
while run_program == "y":

# Input: Asks user for their last name
    last_name = str(input("Enter last name: "))

# Input: Asks user for their distance away from Downtown Chicago
    distance_chicago = int(input("Enter miles away from Downtown Chicago: "))

# Process: Calls the function
    get_train_ticket_price()

# Output: Displays the price for a train ticket
    print("Your ticket costs $",ticket_price)

# Process: Adds each previous train ticket price to the sum ticket price counter
    sum_ticket_price += ticket_price

# Input: Asks user if they want to continue program
    run_program = str(input("Run again? (y/n): "))

# Output: Displays the sum ticket price counter
print("The sum of all tickets is $",sum_ticket_price)
