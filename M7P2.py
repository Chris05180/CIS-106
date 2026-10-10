# Christopher Hernandez  M7P2.py  10/5/26

# Input: Enters the initial value
start_value = int(input("Enter start value: "))

# Input: Enters the stop value
stop_value = int(input("Enter stop value: "))

# Input: Enters the incremental value
increment_value = int(input("Enter increment value: "))

# Process: Adds the incremental value to the starting value while the start value is less than the stop value
while start_value < stop_value:
# Output: Displays the start value
    print(start_value)
    start_value = start_value + increment_value
