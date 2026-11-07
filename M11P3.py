# Christopher Hernandez  M11P3.py  11/4/26

# Process: Sets sales commission as integer variable
sales_commission = int()

# Process: Sets next year target as integer variable
next_year_target = int()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (Y/N): "))

# Process: Creates function that determines sales commission and next year target
def get_sales_report():

# Process: "sales_commission" is treated as global variable
    global sales_commission

# Process: Multiplies number of sales by 10% if number of sales is greater than 100,000
    if number_sales > 100000:
        sales_commission = number_sales * .10

# Process: Multiplies number of sales by 5% if number of sales is less than or equal to 100,000
    elif number_sales <= 100000:
        sales_commission = number_sales * .05

# Process: "next_year_target" is treated as global variable
    global next_year_target

# Process: Multiplies number of sales by 5% to determine next year's target
    next_year_target = number_sales * .05

# Process: Runs program while "Y" is entered
while program_start == "Y":

# Input: Asks for sale person's last name
    last_name = str(input("Enter sales person's last name: "))

# Input: Asks for number of sales
    number_sales = int(input("Enter number of sales: "))

# Process: Calls the function
    get_sales_report()

# Output: Displays sales person's last name, sales commission, and next year's target
    print(f"{last_name}, the commission is ${sales_commission:.2f}\n"
          f"Next year's target is ${next_year_target:.2f}")

# Input: Asks user if they want to run the program again
    program_start = str(input("Run again? (Y/N): "))