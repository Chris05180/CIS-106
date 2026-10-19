# Christopher Hernandez  M8P2.py  10/12/26

# Process: Sets "a" equal to 1
variable_a = 1
# Process: Sets "b" variable b equal to 1
variable_b = 1
# Process: Repeats loop 20 times
for n in range(1,21):
# Output: Displays "a"
    print(variable_a)
# Process: Sets "a" equal to old "b" and "b" to sum of old "a" and old "b"
    variable_a, variable_b = variable_b, variable_a + variable_b
