# Christopher Hernandez  M4P5.py  9/16/2026

# Input: Types in fixed costs
fixed_costs = float(input("Enter fixed costs: $"))

# Input: Types in the price for one unit
price_per_unit = float(input("Enter price per unit: $"))

# Input: Types in the cost to make one item
cost_per_unit = float(input("Enter cost per unit: $"))

# Process: Divides the item's fixed costs by the product of the price per unit and cost per unit
break_even = fixed_costs/(price_per_unit * cost_per_unit)

# Output: Displays amount of money needed to break even
print(f"You need to sell about {break_even:.2f} units to break even")