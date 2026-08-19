

# Part 2: Mini-Project — Expense Report Generator
# The file ../data/expenses.csv tracks personal spending across several categories:
# date,category,description,amount
# 2024-03-01,Food,Grocery store,54.30
# 2024-03-02,Transport,Bus pass,35.00
# ...
# Write a program that analyzes this data and writes a formatted report to a new file. Follow these steps:

# Use os.path.exists() to verify that ../data/expenses.csv exists before opening it. If it doesn't, print an error message and stop.
# Read ../data/expenses.csv into a list of dictionaries using csv.DictReader.
# Convert the amount field to float for each row.
# Filter the list to only rows where category is "Food".
# Calculate the total amount spent on Food.
# Write a report to food_report.txt with this structure:
# First line: Food Expense Report — generated [today's date as "Month DD, YYYY"]
# One line per food expense: [date]: $[amount]
# Last line: Total: $[total to 2 decimal places]
# Hint: All values from csv.DictReader come back as strings. Remember to convert amount with float() before doing any math.

import csv
import os
from datetime import datetime

if not os.path.exists("../data/expenses.csv"):
    print("Error: expenses.csv not found.")
else:
    with open("../data/expenses.csv", "r") as input_file:
        expenses = list(csv.DictReader(input_file))

    for expense in expenses:
        expense["amount"] = float(expense["amount"])

    food_expenses = [
        expense for expense in expenses
        if expense["category"] == "Food"
    ]

    food_total = sum(expense["amount"] for expense in food_expenses)

    report_date = datetime.now().strftime("%B %d, %Y")

    with open("food_report.txt", "w") as output_file:
        output_file.write(
            f"Food Expense Report - generated {report_date}\n"
        )

        for food_expense in food_expenses:
            output_file.write(
                f"{food_expense['date']}: ${food_expense['amount']:.2f}\n"
            )

        output_file.write(f"Total: ${food_total:.2f}\n")