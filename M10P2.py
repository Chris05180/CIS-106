# Christopher Hernandez  M10P2.py  10/28/26

# Process: Sets square footage to be a float value
square_footage = float()

# Input: Asks user if they want to start program
begin_program = str(input("Start program? (Y/N): "))

# Process: Creates a function to determine square footage
def get_square_footage():

# Process: "square footage" is treated as a global
    global square_footage

# Process: Adds the product of room length and height and the product of room width and height
    square_footage = (2 * room_length * room_height) + (2 * room_width * room_height)

# Process: Runs loop while "Y" is entered
while begin_program == "Y":

# Input: Asks for room length
    room_length = float(input("Enter room length: "))

# Input: Asks for room width
    room_width = float(input("Enter room width: "))

# Input: Asks for room height
    room_height = float(input("Enter room height: "))

# Process: Calls the function
    get_square_footage()

# Process: Divides square footage by 50 to determine gallons of paint needed
    paint_gallons = square_footage / 50

# Output: Displays the gallons of paint needed
    print(f"{paint_gallons} gallons of paint are needed")

# Input: Asks user if they want to continue the program
    begin_program = str(input("Run again? (Y/N): "))