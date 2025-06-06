courses = ["GEC 321", "GEC 322", "GEC 323", "GEC 324", "GEC 325", "GEC 326"]
credit_units = [3, 3, 2, 2, 3, 3]
grade_points = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

total_points = 0
total_units = sum(credit_units)

for course, unit in zip(courses, credit_units):
    grade = input(f"What is your grade in {course}?: ").strip().upper()
    total_points += grade_points.get(grade, 0) * unit

gpa = round(total_points / total_units, 2)
print(f"Your GPA is: {gpa}")