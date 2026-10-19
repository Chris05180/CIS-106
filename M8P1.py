# Christopher Hernandez  M8P1.py  10/12/26

# Input: Asks for principal amount
principal_amount = float(input("Enter the principal amount: "))

# Input: Asks for interest rate in decimal form
interest_rate = float(input("Enter the interest rate: "))

# Process: Sets year to 0
year_counter = 0

# Process: Sets interest rate as a float number
total_interest = float()

# Process: Repeats loop 5 times
for n in range(1, 6):
# Process: Multiplies interest rate by principal to get annual interest
    annual_interest = principal_amount * interest_rate
# Process: Adds principal and annual interest to get ending balance
    ending_balance = principal_amount + annual_interest
# Process: Adds 1 to the year counter for every iteration
    year_counter += 1
# Process: Combines each previous annual interest to get total interest
    total_interest += annual_interest
# Output: Displays the year, beginning balance, and ending balance
    print(f"Year     Beginning     Ending \n         "
          f"Balance       Balance \n \n {year_counter}   "
          f"    ${principal_amount:.2f}     ${ending_balance:.2f}")
# Process: Sets the principal to the previous ending balance
    principal_amount = ending_balance

# Output: Displays the total interest
print(f"\nTotal interest earned: ${total_interest:.2f}")
