def evaluate_student(marks):
    if any(mark < 40 for mark in marks):
        print("FAILED")
    else:
        average = sum(marks) / len(marks)
        print("Average marks:", average)

student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

print("Student 1 result:")
evaluate_student(student_1)

print("Student 2 result:")
evaluate_student(student_2)