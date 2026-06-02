# Day 2 - Grade Calculator

# Function to calculate grade
def get_grade(marks):

    # Check for Grade A
    if marks >= 90:
        return "A"

    # Check for Grade B
    elif marks >= 75:
        return "B"

    # Check for Grade C
    elif marks >= 60:
        return "C"

    # Check for Grade D
    elif marks >= 45:
        return "D"

    # Otherwise Grade F
    else:
        return "F"

# List of student marks
students = [95, 82, 67, 50, 30]

# Loop through each student's marks
for marks in students:

    # Calculate grade
    grade = get_grade(marks)

    # Display result
    print("Marks:", marks, "Grade:", grade)

# End of program