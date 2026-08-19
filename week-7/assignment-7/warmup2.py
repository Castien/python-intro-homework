

# Warmup 2: Read a CSV with DictReader
# Use csv.DictReader to read ../data/students.csv — it has three columns: name, subject, and score. 
# Print each student's name and score on a single line:
# Jazmine: 88
# Luis: 74
# Sara: 91
# Marcus: 83
# Priya: 95

import csv
with open("../data/students.csv", "r") as read_students:
    reading = csv.DictReader(read_students)
    for student in reading:
        print(f"{student['name']}: {student['score']}")