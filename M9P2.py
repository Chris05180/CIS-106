# Christopher Hernandez  M9P2.py  10/19/26

# Process: Starts the player counter at 1
player_counter = 1

# Process: Sets the batting average as an integer variable
batting_average = int()

# Input: Asks user if they want to start program
start_program = str(input("Start program? (Y/N): "))

# Process: Creates a function to get the batting average of a player
def get_batting_average():

# Process: "batting_average" is treated as part of the global scope
    global batting_average

# Process: Divides player hits by player at bats to get batting average
    batting_average = player_hits / player_at_bats

# Process: Runs loop while "Y" is entered
while start_program == "Y":

# Input: Enters player's last name
    last_name = str(input("Enter last name: "))

# Input: Enter player's number of hits
    player_hits = int(input("Enter number of hits: "))

# Input: Enter player's number of at bats
    player_at_bats = int(input("Enter number of at bats: "))

# Process: Calls function
    get_batting_average()

# Output: Displays player's last name and batting average
    print(f"{last_name}, your batting average is {batting_average:.2f}")

# Output: Displays amount of players entered
    print(player_counter,"players have been entered")

# Process: Adds 1 to the player counter
    player_counter += 1

# Input: Asks user if they want to continue the program
    start_program = str(input("Run again?: (Y/N) "))