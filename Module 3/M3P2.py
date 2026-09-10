# Christopher Hernandez M3P2 9/9/2026

last_name = input("Enter your last name: ")
# Input student's last name

midterm_score = int(input("Enter your midterm score: "))
# Input student's midterm score

final_exam_score = int(input("Enter your final exam score: "))
# Input student's final exam score

total_exam_score = midterm_score * .40 + final_exam_score * .60
# Add 40% of student's midterm score and 60% of final exam score

print(f"{last_name}, your score is {total_exam_score:.1f}")
# Display student's last name and their total exam score