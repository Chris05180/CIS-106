# Christopher Hernandez  M9P4.py  10/21/26

# Process: Sets sum gross pay counter to 0
sum_gross_pay = 0

# Process: Defines employee pay rate as integer value
pay_rate = int()

# Input: Asks user if they want to start program
start_program = str(input("Run program? Y or N: "))

# Process: Creates a function
def get_pay_rate():

# Process: "pay_rate" is treated as part of global scope
    global pay_rate

# Process: Sets pay rate to $25 if job code entered is "L"
    if job_code == "L":
        pay_rate = 25

# Process: Sets pay rate to $30 if job code entered is "A"
    elif job_code == "A":
        pay_rate = 30

# Process: Sets pay rate to $50 if job code entered is "J"
    elif job_code == "J":
        pay_rate = 50

# Process: Runs program while "Y" is entered
while start_program == "Y":

# Input: Enters employee's last name
    last_name = str(input("Enter last name: "))

# Input: Enters employee's job code
    job_code = str(input("Enter job code: "))

# Input: Enters employee's hours worked
    hours_worked = int(input("Enter hours worked: "))

# Process: Calls function
    get_pay_rate()

# Process: Multiplies pay rate by hours worked to get employee gross pay
    gross_pay = pay_rate * hours_worked

# Process: Calculates overtime pay if hours worked is above 40
    if hours_worked > 40:

# Process: Multiplies employee pay rate by 1.5 to get overtime pay
        overtime_rate = pay_rate * 1.5

# Process: Subtracts 40 from hours worked to get overtime hours
        overtime_hours = hours_worked - 40

# Process: Multiplies overtime rate by overtime hours to get overtime pay
        overtime_pay = overtime_rate * overtime_hours

# Process: Sets overtime pay equal to pay rate if hours worked is not above 40
    else:
        overtime_pay = pay_rate

# Output: Displays employee's last name and gross pay
    print(f"{last_name}, your gross pay is ${gross_pay}")

# Process: Displays employee's overtime pay if hours worked is above 40
    if hours_worked > 40:
        print("With overtime you made $",overtime_pay)

# Process: Sums up employee's gross pay by adding each previous gross pay
    sum_gross_pay += gross_pay

# Input: Asks user if they want to continue program
    start_program = str(input("Run again? Y or N: "))

# Process: Displays the sum of employee's gross pay
print("The sum of all employee gross sums is $",sum_gross_pay)
