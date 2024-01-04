# Given dictionary of student scores
student_scores = {
    "RAVI": 86,
    "VIPIN": 93,
    "CHANDAR": 79,
    "KULDEEP": 89,
    "NAMAN": 96
}

# i. Find and print the student with the highest score
highest_scorer = max(student_scores, key=student_scores.get)
print(f"The student with the highest score is: {highest_scorer} with a score of {student_scores[highest_scorer]}")

# ii. Calculate and print the average score for all students
average_score = sum(student_scores.values()) / len(student_scores)
print(f"The average exam score for all students is: {average_score:.2f}")

# iii. Create a new dictionary passing_students with scores 75 or higher
passing_students = {name: score for name, score in student_scores.items() if score >= 75}
print("Students who scored 75 or higher:")
print(passing_students)
