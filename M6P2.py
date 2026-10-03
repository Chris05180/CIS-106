# Christopher Hernandez  M6P2.py  9/28/26

# Input: Enters the part's number
part_number = str(input("Enter the part number: "))

# Input: Enters amount of parts bought
part_quantity = int(input("Enter quantity of parts: "))

# Process: Sets the price at $1 if part "10" or "55" are bought
if part_number == "10" or part_number == "55":
    unit_cost = 1
# Process: Sets the price at $2 if part "99" is bought
elif part_number == "99":
    unit_cost = 2
# Process: Sets the price at $3 if part "70" or "80" are bought
elif part_number == "70" or part_number == "80":
    unit_cost = 3
# Process: Sets the price at $5 if a different part is bought
else:
    unit_cost = 5

# Process: Multiplies the amount of parts bought by their price
total_cost = unit_cost * part_quantity

# Output: Displays the part number, price, and cost of parts bought
print(f"Part {part_number} costs ${unit_cost} per unit for a total"
      f" of ${total_cost:.2f}")

