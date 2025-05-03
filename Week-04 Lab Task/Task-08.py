#Q8: Tuple Unpacking for Student Grades 
 
# Given a list of tuples (student, grade), display all students with their scores.

grades = [("Ali", 85), ("Sara", 90), ("Jhon", 78)]

for name, score in grades:
    print(f"{name} scored {score}")