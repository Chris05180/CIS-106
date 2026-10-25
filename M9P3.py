# Christopher Hernandez  M9P3.py  10/19/26

# Process: Sets the trip counter to 1
trip_counter = 1

# Process: Defines miles per gallon as a float variable
miles_per_gallon = float()

# Input: Asks user if they want to start program
program_start = str(input("Begin program? (YES/NO): "))

# Process: Creates function to get miles per gallon
def get_miles_per_gallon():

# Process: "miles_per_gallon" is treated as part of the global scope
    global miles_per_gallon

# Process: Divides amount of miles traveled by amount of gallons used
    miles_per_gallon = miles_travelled / gallons_used

# Process: Runs loop while "YES" is entered
while program_start == "YES":

# Input: Enters name of city destination
    destination_city = str(input("Enter city: "))

# Input: Enters amount of miles driven
    miles_travelled = float(input("Enter miles driven: "))

# Input: Enters amount of gallons used
    gallons_used = float(input("Enter gallons used: "))

# Process: Calls function
    get_miles_per_gallon()

# Output: Displays miles traveled, city, and miles per gallon
    print(f"You traveled {miles_travelled:.2f} miles to {destination_city} "
          f"and used up {miles_per_gallon:.2f} miles per gallon.")

# Output: Displays amount of trips made
    print("You have made",trip_counter,"trips")

# Process: Adds 1 to the trip counter
    trip_counter += 1

# Input: Asks user if they want to continue program
    program_start = str(input("Again? (YES/NO): "))