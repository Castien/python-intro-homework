

# Write a function is_valid_score(score) 
# that returns True if score is an integer between 0 and 100 (inclusive), and False otherwise. 
# Then use input() to ask the user for a score. 
# Call your function inside an if statement and print either "Valid score." 
# or "Invalid score — must be between 0 and 100.".

# Write a function is_valid_score(score):
#  returns True if score is an integer between 0 and 100 (inclusive), and False otherwise. 
def is_valid_score(score):
    return isinstance(score, int) and 0 <= score <= 100

# Then use input() to ask the user for a score.
score = int(input("Enter a whole number score: "))

# Call your function inside an if statement
# print either "Valid score." or "Invalid score — must be between 0 and 100.".
if is_valid_score(score):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")

# Enter score: 50 
# Valid score.

# Enter a whole number score: 125
# Invalid score — must be between 0 and 100.

# Enter score: 2.3
# ValueError: invalid literal for int() with base 10: '2.3'