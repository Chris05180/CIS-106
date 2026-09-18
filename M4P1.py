# Christopher Hernandez  M4P1.py  9/14/2026

# Input: Types in exam 1 score
exam_one_score = float(input("Type in your first score: "))

# Input: Types in exam 2 score
exam_two_score = float(input("Type in your second score: "))

# Process: Multiplies 60% of exam 1 score, multiplies 40% of exam 2 score, and adds the result
total_score = (.60 * exam_one_score) + (.40 * exam_two_score)

# Output: Displays the sum of exam 1 and exam 2
print(f"Your total score is {total_score:.2f}!")