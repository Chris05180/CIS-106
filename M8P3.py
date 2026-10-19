# Christopher Hernandez  M8P3.py  10/12/26

# Process: Sets the sum of all bonuses as integer value
sum_bonus = int()

# Process: Opens and closes text file to read it
with open('M8P3FILE.txt', 'r') as f:

# Process: While true, reads one line and removes blank line
    while 1==1:
        last_name = f.readline().strip()
# Process: Terminates nearest enclosing loop
        if not last_name:
            break
# Process: Reads one line, turns it into integer value, and removes blank line
        salary = int(f.readline().strip())
# Process: Sets bonus rate to .20 if salary is equal to or greater than $100,000
        if salary >= 100000:
            bonus_rate = .20
# Process: Sets bonus rate to .15 if salary is equal to $50,000
        elif salary == 50000:
            bonus_rate = .15
# Process: Sets bonus rate to .10 if salary is anything else
        else:
            bonus_rate = .1
# Process: Multiplies employee's salary by bonus rate to get employee bonus
        employee_bonus = salary * bonus_rate
# Process: Sums up employee bonuses by adding each previous employee bonus
        sum_bonus += employee_bonus
# Output: Displays employee's last name, salary, and bonus rate
        print(f"{last_name}, has a ${salary:.2f} salary and a bonus "
              f"of ${employee_bonus:.2f}")

# Output: Displays sum of all employee bonuses
print(f"The sum of all bonuses is ${sum_bonus:.2f}")
