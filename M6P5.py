# Christopher Hernandez  M6P5.py  9/29/26

# Input: Enters the employee's name
employee_name = str(input("Enter your name: "))

# Input: Enters the employee's salary
salary = float(input("Enter your salary: "))

# Input: Enters the employee's job level
job_level = int(input("Enter your job level: "))

# Process: Sets the bonus rate to be 25 if the job level is equal to or greater than 10
if job_level >= 10:
    bonus_rate = 25
# Process: Sets the bonus rate to be 20 if the job level is between 9 and 5
elif 9 >= job_level >= 5:
    bonus_rate = 20
# Process: Sets the bonus rate to be 10 if the job level is the job level is anything else
else:
    bonus_rate = 10

# Process: Multiplies the employee's salary by the bonus rate which is turned into a decimal
bonus_amount = salary * (bonus_rate/100)

# Output: Displays the employee's name and bonus
print(f"{employee_name}, your bonus is ${bonus_amount:.2f}")