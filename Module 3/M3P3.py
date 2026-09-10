# Christopher Hernandez M3P3 9/9/26

your_amount = float(input("$"))
# Input your amount received from job

friend1_amount = float(input("$"))
# Input friend 1's amount

friend2_amount = float(input("$"))
# Input friend 2's amount

split_amount = (your_amount + friend1_amount + friend2_amount) / 3
# Add up everyone's amount and divide by 3

print(f"You each receive ${split_amount:.2f}")
# Display the even amount everyone will receive
