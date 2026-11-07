# Christopher Hernandez M11P4.py  11/4/26

# Process: Sets average score as integer variable
average_score = int()

# Process: Sets handicap score as integer variable
handicap_score = int()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (Y/N): "))

# Process: Creates function that determines average score and handicap score
def get_average_bowling_score():

# Process: "average_score" is treated as global variable
    global average_score

# Process: Sums up 3 game scores and divides them by 3
    average_score = (score_one + score_two + score_three)/3

# Process: "handicap_score" is treated as global variable
    global handicap_score

# Process: Subtracts 200 from  the average score and multiplies it by 90% to determine handicap score
    handicap_score = (200 - average_score) * .90

# Process: Runs program while "Y" is entered
while program_start == "Y":

# Input: Asks for user's last name
    last_name = str(input("Enter last name: "))

# Input: Asks for game one's score
    score_one = int(input("Enter score for game 1: "))

# Input: Asks for game two's score
    score_two = int(input("Enter score for game 2: "))

# Input: Asks for game three's score
    score_three = int(input("Enter score for game 3: "))

# Process: Calls function
    get_average_bowling_score()

# Output: Displays user's last name, average score, and handicap score
    print(f"{last_name}, your average score is {average_score:.2f}\n"
          f"Your average score with handicap is {handicap_score:.2f}")

# Input: Asks user if they want to run the program again
    program_start = str(input("Run again? (Y/N): "))