# Christopher Hernandez  M5P4.py  9/22/26

# Input: Enters the appliance's name
name_appliance = str(input("Enter appliance: "))

# Input: Enters the appliance's cost
cost_appliance = float(input("Enter appliance cost: "))

# Process: Multiplies the appliance's cost by 10% to determine the warranty
if cost_appliance > 1000:
    cost_warranty = .10 * cost_appliance
# Process: Multiplies the appliance's cost by 5% to determine the warranty
else:
    cost_warranty = .05 * cost_appliance

# Process: Adds the appliance's cost and the appliance's warranty
total_cost = cost_appliance + cost_warranty

# Output: Displays the appliance's name and cost
print(f"The {name_appliance} costs ${cost_appliance:.2f}"
      f" without warranty")

# Output: Displays the appliance's cost with warranty and the warranty
print(f"The total is ${total_cost:.2f} with a ${cost_warranty:.2f} "
      f"warranty")