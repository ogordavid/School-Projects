def main():
    print("CGPA Calculator")
    semesters = int(input("How many semesters? "))
    total_points = 0
    total_credits = 0
    for i in range(1, semesters + 1):
        gpa = float(input(f"Enter GPA for semester {i}: "))
        credits = int(input(f"Enter credit units for semester {i}: "))
        total_points += gpa * credits
        total_credits += credits
    cgpa = total_points / total_credits
    print(f"Your CGPA is: {cgpa:.2f}")
if __name__ == "__main__":
    main()