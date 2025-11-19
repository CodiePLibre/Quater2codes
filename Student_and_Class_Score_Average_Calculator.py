num_stu = int(input("Enter number of students: "))
num_sub = int(input("Enter number of subjects: "))

total_sum = 0
total_scores = 0

for student in range(1, num_stu + 1):
    print(f"Student {student}")
    student_sum = 0
    for subject in range(1, num_sub + 1):
        score = float(input(f"Enter score {subject}: "))
        student_sum += score
    student_average = student_sum / num_sub
    print(f"Average for Student {student} = {student_average}")
    total_sum += student_sum
    total_scores += num_sub

class_average = total_sum / total_scores
print(f"Class Average = {class_average}")
