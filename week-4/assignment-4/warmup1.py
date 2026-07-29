# A data file is provided in week-4/data/roster.py. 
# Copy the students list from that file into your script — it contains dictionaries with name, score, and subject fields.
# Using loops and data structure operations, your script must:

# Find the top scorer — loop through the list and track the highest score and the name that goes with it. 
# Do not use Python's built-in max() on the list directly.
# Calculate the class average — accumulate the total score in a loop, then divide.
# List all unique subjects — use a set to collect subjects as you loop, then print them.
# List high scorers — use a use a loop and .append() to get the names of all students who scored above 75.

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Variables
top_student = ""
top_score = 0
total_score = 0

# Variable for all unique subjects
subjects = set()

# Variable for high scorers
high_scorers = []


# Loop through students
for student in students:

    # Find highest score
    if student["score"] > top_score:
        top_score = student["score"]
        top_student = student["name"]

    # Add score to total
    total_score += student["score"]

    # Add subject to set
    subjects.add(student["subject"])

    # Add high scorers
    if student["score"] > 75:
        high_scorers.append(student["name"])


# Calculate average
class_average = total_score / len(students)


# Print results
print(f"Top scorer:       {top_student} ({top_score})")
print(f"Class average:    {class_average:.1f}")
print(f"Subjects offered: {subjects}")
print(f"High scorers:     {high_scorers}")