
# Write a script that:

# Asks the user to enter a temperature in Fahrenheit:
fahrenheit = float(input("Please input temperature in Fahrenheit: "))

# Converts it to Celsius using the formula: celsius = (fahrenheit - 32) * 5 / 9:
celsius = (fahrenheit - 32) * 5 / 9

# Prints the result rounded to one decimal place: (:.1f)
print(f"{fahrenheit:.1f}°F is {celsius:.1f}°C.")

# Enter a temperature in Fahrenheit: 72
# 72.0°F is 22.2°C.

# Requirements:
# Handle the conversion yourself (no built-in converter functions)
# Use an f-string for the output
# Round to exactly one decimal place
# Save as: mini_project.py

