# Christopher Hernandez  M10P3.py  10/28/26

# Process: Sets the car MSRP counter to 0
car_msrp_counter = 0

# Process: Sets the total car price counter to 0
total_price_counter = 0

# Process: Defines total car price as a float value
total_car_price = float()

# Input: Asks user if they want to start program
start_program = str(input("Start Program? (Yes/No): "))

# Process: Creates a function to determine the car's out the door price
def get_out_door_price():

# Process: "total_car_price" is treated as a global
    global total_car_price

# Process: Sets the percent off at 10% if "Honda" and "Accord" are typed
    if car_make == "Honda" and car_model == "Accord":
        percent_off = .10

# Process: Sets the percent off at 15% if "Toyota" and "Rav4" are typed
    elif car_make == "Toyota" and car_model == "Rav4":
        percent_off = .15

# Process: Sets the percent off at 30% if "Y" is typed for the electric vehicle code
    elif electric_vehicle_code == "Y":
        percent_off = .30

# Process: Sets the percent off at 5% if anything else typed
    else:
        percent_off = .05

# Process: Discount is subtracted from MSRP and combined with 7% tax to get total car price
    total_car_price = (car_msrp - (car_msrp * percent_off)) + (car_msrp * .07)

# Process: Runs program while "Yes" is entered
while start_program == "Yes":

# Input: Asks for car manufacturer
    car_make = str(input("Enter car manufacturer: "))

# Input: Asks for car model
    car_model = str(input("Enter car model: "))

# Input: Asks if car is an electric vehicle
    electric_vehicle_code = str(input("Electric vehicle? (Y/N): "))

# Input: Asks for the car's MSRP
    car_msrp = float(input("Enter price of car: "))

# Process: Calls the function
    get_out_door_price()

# Output: Displays the total car price
    print(f"The total car price is ${total_car_price:.2f}")

# Process: Adds each previous car MSRP to the car MSRP counter
    car_msrp_counter += car_msrp

# Process: Adds each previous total car price to the total car price counter
    total_price_counter += total_car_price

# Input: Asks user if they want to continue program
    start_program = str(input("Continue? (Yes/No): "))

# Output: Displays the car MSRP counter
print(f"The sum of all car MSRP's is ${car_msrp_counter:.2f}")

# Output: Displays the car total car price counter
print(f"The sum of all total car price's is ${total_price_counter:.2f}")
