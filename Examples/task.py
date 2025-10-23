score = int(input("Enter the student's score (0-100): "))
grade = ""

# First condition is already completed!
if score >= 80 and score <= 100:
    grade = "A"
# -------- Help Mr. Thompson below! -----------

elif score >= 60:
    grade = "B"

elif score >= 50:
    grade = "C"

elif score >= 40:
    grade = "D"

elif score >= 0:
    grade = "Fail"


# -------- Help Mr. Thompson above here! -----------


print("\n According to my notes... that's a " + grade + " grade!")