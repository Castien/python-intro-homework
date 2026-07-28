

# Use input() to ask the user for their age. 
# Convert it to an integer, then use if/elif/else with 'and' to check ranges and print which category they fall into:
# Age range	Category
# 0-12	    Child
# 13-17 	Teen
# 18-64 	Adult
# 65andUp  	Senior

age = int(input("Enter your age: "))

if age >= 0 and age <= 12:
    print("You are a Child.")
elif age >= 13 and age <= 17:
    print("You are a Teen.")
elif age >= 18 and age <= 64:
    print("You are an Adult.")
elif age >= 65:
    print("You are a Senior.")
else:
    print("Invalid entry, please input your age as a number.")

