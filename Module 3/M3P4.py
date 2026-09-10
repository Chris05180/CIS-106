# Christopher Hernandez M3P4 9/9/26

car_make = input("Enter car brand: ")
# Input manufacturer of the car

car_model = input("Enter car model: ")
# Input model of the car

car_msrp = float(input("Enter price of car: $"))
# Input the car's MSRP

discount_percentage = float(input("Enter discount: "))
# Input the car's discount percentage as a decimal

amount_off = car_msrp * discount_percentage
# Multiplies the car's MSRP by the car's discount percentage

discounted_price = car_msrp - amount_off
# Subtract the amount off the car from the car's MSRP

print(f"{car_make} {car_model} ${car_msrp:.2f} {discount_percentage*100:.2f}% ${amount_off:.2f} ${discounted_price:.2f}")
# Displays car's brand, model, discount percentage as a %, amount off, and discounted price