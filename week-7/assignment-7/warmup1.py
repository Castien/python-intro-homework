

# Warmup 1: Read a Text File Line by Line
# Open ../data/notes.txt using a with block, read it line by line, and print each line with its number:
# Line 1: Python is great for working with files.
# Line 2: You can read, write, and append text.
# Line 3: The 'with' statement keeps things clean.
# Line 4: Always close your files when you're done.
# Use .strip() to remove the trailing newline from each line before printing.

with open("../data/notes.txt", "r") as read_notes:
    num = 1
    for line in read_notes:
        print(f"Line {num}: {line.strip()}")
        num += 1
