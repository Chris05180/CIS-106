# Christopher Hernandez  M5P5.py  9/23/26

# Input: Enters user's last name
last_name = str(input("Enter your last name: "))

# Input: Enters number of dependents
dependents = int(input("Enter number of dependents: "))

# Input: Enters gross income
gross_income = float(input("Enter your gross income: "))

# Process: Subtracts the product of the number of dependents and $12000 from gross income to get adjusted gross income
adjust_income = gross_income - dependents * 12000

# Process: Sets the tax rate at 10% if gross income is above $50000
if gross_income > 50000:
    tax_rate = .20
# Process: Sets the tax rate at 20% if gross income is or below $50000
else:
    tax_rate = .10

# Process: Multiplies the adjusted gross income by the tax rate to get the income tax
income_tax = adjust_income * tax_rate

# Process: Sets the income tax at $100 if income is negative
if income_tax < 0:
    income_tax = 100

# Output: Displays the user's name, number of dependents, and gross income
print(f"{last_name} you have {dependents} "
      f"dependents and an income of ${gross_income:.2f}")

# Output: Displays the adjusted gross income and the income tax
print(f"You have an adjusted gross income of ${adjust_income:.2f} "
      f"and an income tax of ${income_tax:.2f}")