# Christopher Hernandez  M10P5.py  10/28/26

# Process: Sets the sum market value counter to 0
sum_market_value = 0

# Process: Sets the sum assessed value counter to 0
sum_assessed_value = 0

# Process: Defines assessed values as float value
assessed_value = float()

# Process: Defines assessed value percent as float value
assessed_value_percent = float()

# Input: Asks user if they want to start program
run_program = str(input("Begin program? (YES/NO): "))

# Process: Creates function to determine the assessed value
def get_assessed_value():

# Process: Treats "assessed_value" as a global
    global assessed_value

# Process: Treats "assessed_value_percent" as a global
    global assessed_value_percent

# Process: Sets the percent to 90% if "Cook" is typed for county
    if user_county == "Cook":
        assessed_value_percent = .90

# Process: Sets the percent to 80% if "DuPage" is typed for county
    elif user_county == "DuPage":
        assessed_value_percent = .80

# Process: Sets the percent to 75% if "McHenry" is typed for county
    elif user_county == "McHenry":
        assessed_value_percent = .75

# Process: Sets the percent to 60% if "Kane" is typed for county
    elif user_county == "Kane":
        assessed_value_percent = .60

# Process: Sets the percent to 70% if anything else is typed for county
    else:
        assessed_value_percent = .70

# Process: Multiplies the market value by assessed value percent to get assessed value
    assessed_value = market_value * assessed_value_percent

# Process: Runs program while "YES" is entered
while run_program == "YES":

# Input: Asks user for their county
    user_county = str(input("Enter your county: "))

# Input: Asks user for their counties market value
    market_value = float(input("Enter your market value: "))

# Process: Calls the function
    get_assessed_value()

# Output: Displays the assessed value
    print(f"The market value in this county is ${assessed_value:.2f}")

# Process: Adds each previous market value to the sum market value counter
    sum_market_value += market_value

# Process: Adds each previous assessed value to the sum assessed value counter
    sum_assessed_value += assessed_value

# Input: Asks user if they want to continue program
    run_program = str(input("Again? (YES/NO): "))

# Output: Displays the sum market value
print(f"The sum of all market values is ${sum_market_value:.2f}")

# Output: Displays the sum assessed value
print(f"The sum of all assessed values is ${sum_assessed_value:.2f}")