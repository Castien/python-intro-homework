

# Warmup 2: Input Validation with a While Loop
# Use a while loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop:
# Enter a positive integer: -3
# That's not a positive integer. Try again.
# Enter a positive integer: hello
# That's not a positive integer. Try again.
# Enter a positive integer: 7
# Got it: 7
# Hint: You'll need try/except to handle non-numeric input — or you can check str.isdigit().


#str.isdigit() version

while True:
    # storing user input as string
    user_input = input("Enter a positive integer: ")

    # check if input is only digits and is greater than 0
    if user_input.isdigit() and int(user_input) > 0:
        print(f"Got it: {user_input}.")

        # if True, while loop ends
        break
    else:
        # input is not valid, ask for new input
        print("That's not a positive integer. Try again.")

# try/except version
while True:
    try:
        # convert and store user input as integer
        number = int(input("Enter a positive integer: "))

        # check if number is greater than 0
        if number > 0:
            print(f"Got it: {number}.")

        # if True, while loop ends
            break
        else:
            # input is not greater than zero, ask for new input
            print("That's not a positive integer. Try again.")

    # runs if user input isn't a number
    except ValueError:
        print("That's not a positive integer. Try again.")