# Christopher Hernandez  M11P2.py  11/4/26

# Process: Sets average score as float variable
average_score = float()

# Process: Sets total points as float variable
total_points = float()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (Y/N): "))

# Process: Creates function that determines average score and total points
def get_average_total_points():

# Process: "average_score" is treated as global variable
    global average_score

# Process: Sums up the 3 exam scores and divides them by 3
    average_score = (exam_one+ exam_two + exam_three) / 3

# Process: "total_points" is treated as global variable
    global total_points

# Process: Sums up the 3 exam scores
    total_points = exam_one + exam_two + exam_three

# Process: Runs program while "Y" is entered
while program_start == "Y":

# Input: Asks for user's last name
    last_name = str(input("Enter your last name: "))

# Input: Asks for exam one's score
    exam_one = int(input("Enter exam 1 score: "))

# Input: Asks for exam two's score
    exam_two = int(input("Enter exam 2 score: "))

# Input: Asks for exam three's score
    exam_three = int(input("Enter exam 3 score: "))

# Process: Calls function
    get_average_total_points()

# Output: Displays user's last name, total exam points, and average exam score
    print(f"{last_name}, you have {total_points} points \n"
          f"Your average score is {average_score:.2f}")

# Input: Asks user if they want to run the program again
    program_start = str(input("Run again? (Y/N): "))