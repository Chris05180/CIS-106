# Christopher Hernandez  M4P4.py  9/15/2026

# Input: Types in the first name of person
first_name = str(input("Type in your first name: "))

# Input: Types in the amount of steps walked in a day
steps_walked = int(input("Type in number of steps walked today: "))

# Process: Multiplies amount of steps walked by .25
calories_burned = steps_walked * .25

# Output: Displays amount of calories burned
print(f"{first_name}, you burned {calories_burned:.0f} calories today!")