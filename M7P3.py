# Christopher Hernandez  M7P3.py  10/5/26

# Input: Enters YES to start program or No to not start it
program_start = str(input("Start Program? YES/NO: "))

# Process: Sets the student counter to 0
count_students = 0

# Process: Starts the program while YES is entered
while program_start == "YES":
# Process: Adds 1 to the student counter
    count_students = count_students + 1
# Input: Enters the student's last name
    last_name = str(input("Enter last name: "))
# Input: Enters student's first exam score
    exam_one = int(input("Enter exam one score: "))
# Input: Enters student's second exam score
    exam_two = int(input("Enter exam two score: "))
# Process: Adds both exam scores and divides them by 2 to get average
    average_score = (exam_one + exam_two) / 2
# Output: Displays the student's last name and average
    print(last_name,", your average exam score is",average_score)
# Input: Enters YES to continue programs or NO to not continue
    program_start = str(input("Continue program? YES/NO: "))

# Output: Displays the student counter
print(count_students,"students entered data")