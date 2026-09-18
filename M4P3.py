# Christopher Hernandez  M4P3.py  9/15/2026

# Input: Type in the meal total
meal_total = float(input("Type in meal total: $"))

# Process: Multiplies meal total with 15% tip
tip_value_one = meal_total * .15

# Process: Multiplies meal total with 18% tip
tip_value_two = meal_total * .18

# Process: Multiplies meal total with 20% tip
tip_value_three = meal_total * .20

# Process: Adds up meal total with 15% tip
meal_tip_one = meal_total + tip_value_one

# Process: Adds up meal total with 18% tip
meal_tip_two = meal_total + tip_value_two

# Process: Adds up meal total with 20% tip
meal_tip_three = meal_total + tip_value_three

# Output: Displays the meal total, the 15% tip, and the sum of the meal and 15% tip
print(f"With 15% tip:\n"
      f"Total: ${meal_total:.2f}\n"
      f"Tip: ${tip_value_one:.2f}\n"
      f"Total With Tip: ${meal_tip_one:.2f}\n")

# Output: Displays the meal total, the 18% tip, and the sum of the meal and 18% tip
print(f"With 18% tip:\n"
      f"Total: ${meal_total:.2f}\n"
      f"Tip: ${tip_value_two:.2f}\n"
      f"Total With Tip: ${meal_tip_two:.2f}\n")

# Output: Displays the meal total, the 20% tip, and the sum of the meal and the 20% tip
print(f"With 20% tip:\n"
      f"Total: ${meal_total:.2f}\n"
      f"Tip: ${tip_value_three:.2f}\n"
      f"Total With Tip: ${meal_tip_three:.2f}\n")