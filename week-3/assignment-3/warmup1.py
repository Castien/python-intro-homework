

# Warmup 1: Letter Grades
# Start with a hardcoded score variable (pick any number 0-100). 
# Use if/elif/else to print the corresponding letter grade:
# Score	Grade
# 90-100	A
# 80-89 	B
# 70-79	    C
# 60-69	    D
# Below 60	F

score = 95

if score >= 90:
    print(f"Score: {score}")
    print("Grade: A")
elif score >= 80:
    print(f"Score: {score}")
    print("Grade: B")
elif score >= 70:
    print(f"Score: {score}")
    print("Grade: C")
elif score >= 60:
    print(f"Score: {score}")
    print("Grade: D")
else:
    print(f"Score: {score}")
    print("Grade: F")

