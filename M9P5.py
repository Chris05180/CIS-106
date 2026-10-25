# Christopher Hernandez  M9P5.py  10/21/26

# Process: Sets sum tuition counter to 0
sum_tuition = 0

# Process: Defines student's tuition amount as float variable
tuition_owed = float()

# Process: Defines cost per credit hour as float variable
cost_per_credit = float()

# Input: Asks user if they want to start the program
start_program = str(input("Start program? Y or N: "))

# Process: Creates a function
def get_tuition_owed():

# Process: "tuition_owed" is treated as part of the global scope
    global tuition_owed

# Process: "cost_per_credit" is treated as part of the global scope
    global cost_per_credit

# Process: Sets the cost per credit at $250 if district code is "I"
    if district_code == "I":
        cost_per_credit = 250

# Process: Sets the cost per credit at $550 if district code is "O"
    elif district_code == "O":
        cost_per_credit = 550

# Process: Multiplies student's credit hours by cost per credit
    tuition_owed = credit_hours * cost_per_credit

# Process: Runs loop while "Y" is entered
while start_program == "Y":

# Input: Enters student's last name
    last_name = str(input("Enter your last name: "))

# Input: Enters student's credit hours
    credit_hours = int(input("Enter your credit hours: "))

# Input: Enters student's district code
    district_code = str(input("Enter your district code: "))

# Process: Calls function
    get_tuition_owed()

# Output: Displays student's last name and tuition owed
    print(f"{last_name}, you owe ${tuition_owed} in tuition")

# Process: Adds previous tuition owed by students to sum of tuition
    sum_tuition += tuition_owed

# Input: Asks user if they want to run program again
    start_program = str(input("Run again? Y or N: "))

# Output: Displays the sum of all students tuition
print("A total sum of $",sum_tuition,"is owed in tuition")
