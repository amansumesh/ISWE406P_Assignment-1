# Program 2

score = float(input("Enter the student's score: "))

if score >= 95:
    grade = "A+"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)
