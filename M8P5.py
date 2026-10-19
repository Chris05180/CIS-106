# Christopher Hernandez  10/15/26  M8P5.py

# Process: Sets the student counter to 0
student_counter = 0

# Process: Sets the sum of all student tuition to float value
sum_tuition_owed = float()

# Process: Opens and closes text file to read it
with open('M8P5FILE.txt', 'r') as f:
# Process: While true, reads one line and removes blank line
    while 1==1:
        last_name = f.readline().strip()
# Process: Terminates closest enclosing loop
        if not last_name:
            break
# Process: Reads one line, turns it into string value, and removes blank line
        district_code = str(f.readline().strip())
# Process: Reads one line, turns it into integer value, and removes blank line
        student_credits = int(f.readline().strip())
# Process: Sets cost per credit to $250 if district code is "I"
        if district_code == "I":
            cost_per_credit = 250
# Process: Sets cost per credit to $500 if district code is "O"
        elif district_code == "O":
            cost_per_credit = 500
# Process: Multiplies student's credits by cost per credit to get student's tuition
        tuition_owed = student_credits * cost_per_credit
# Output: Displays student's last name, credits, and the cost per credit
        print(f"{last_name}, has {student_credits} credits and "
              f"owes ${tuition_owed} in tuition")
# Process: Adds 1 to the student counter each time loop is repeated
        student_counter += 1
# Process: Sums up all of student's tuition by adding each previous student's tuition
        sum_tuition_owed += tuition_owed

# Output: Displays the sum of all student's tuition and amount of students
print(f"There are {student_counter} students \nThe sum of all "
      f"students tuition is ${sum_tuition_owed:.2f}")