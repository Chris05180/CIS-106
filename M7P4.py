# Christopher Hernandez  M7P4.py  10/5/26

# Input: Enters YES to start program or No to not start it
program_start = str(input("Start Program? YES/NO: "))

# Process: Sets gross pay as a float variable
gross_pay = float()

# Process: Sets the employee's combined gross pay to 0
sum_pay  = 0

# Process: Sets the employee counter to 0
employee_counter = 0

# Process: Starts the program while YES is entered
while program_start == "YES":
# Process: Adds 1 to the employee counter
    employee_counter = employee_counter + 1
# Input: Enters employee's last name
    last_name = str(input("Enter last name: "))
# Input: Enters employee's amount of hours worked
    hours_worked = float(input("Enter amount of hours worked: "))
# Input: Enters employee's rate of pay
    pay_rate = float(input("Enter rate of pay: "))
# Process: Multiplies employee's hours worked and pay rate
    gross_pay = hours_worked * pay_rate
# Process: Displays "You have time off" if employee's hours worked is greater than 40
    if hours_worked > 40:
        print("You have time off")
# Process: Sums up the gross pay for each gross pay entered
    sum_pay += gross_pay
# Output: Displays employee's last name and gross pay
    print(f"{last_name}, your gross pay is ${gross_pay:.2f}")
# Input: Asks user if they want to continue the program through a YES or NO
    program_start = str(input("Continue Program? YES/NO: "))

# Output: Displays the number of employees and the sum gross pay
print(f"There are {employee_counter} employees and the sum gross "
      f"pay is ${sum_pay:.2f}")

# Process: Divides the employee's combined gross pay by the number of employees
average_pay = sum_pay/employee_counter

# Output: Displays employee's average pay
print(f"The average pay for an employee is ${average_pay:.2f}")

