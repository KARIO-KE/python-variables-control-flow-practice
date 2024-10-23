score = int(input("Please enter score for grading: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = None
if grade is not None:
    print(f"Your grade is: {grade}")
else:
    print("Invalid score! Enter the correct score.")
