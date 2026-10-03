# Christopher Hernandez  M6P3.py  9/28/26

# Input: Enters the CD's principal amount
cd_principle = float(input("Enter principle: "))

# Input: Enters the CD's years to maturity
year_maturity = int(input("Enter years to maturity: "))

# Process: Sets the interest rate at 6 if principal is greater than $100,000 and 5 years to maturity
if cd_principle > 100000 and year_maturity == 5:
    interest_rate = 6
# Process: Sets the interest rate at 5 if principal is between $100,000 or $50,000 and 10 years to maturity
elif 100000 >= cd_principle >= 50000 and year_maturity == 10:
    interest_rate = 5
# Process: Sets the interest rate at 5 if principal is between $100,000 or $50,000 and 5 years to maturity
elif 100000 >= cd_principle >= 50000 and year_maturity == 5:
    interest_rate = 4
# Process: Sets the interest at 2 if principal and years to maturity is anything different
else:
    interest_rate = 2

# Process: The interest rate becomes a decimal and is multiplied by the CD's principal
interest_amount = (interest_rate/100) * cd_principle

# Output: Displays the CD's principal, interest amount, and interest rate
print(f"Your principle of ${cd_principle:.2f} has grown to"
      f" ${interest_amount:.2f} at a {interest_rate}% interest rate")