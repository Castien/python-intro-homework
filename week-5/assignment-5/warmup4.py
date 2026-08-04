

# Warmup 4: FizzBuzz
# Loop from 1 to 30 and print one word per line:

# "FizzBuzz" if the number is divisible by both 3 and 5
# "Fizz" if divisible by 3 only
# "Buzz" if divisible by 5 only
# The number itself otherwise
# Check the combined case first.

# loop through numbers 1 to 30, stops at 31
for number in range(1, 31):

    # check if number divisible by both 3 and 5
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    # check if number is divisible by 3 only
    elif number % 3 == 0:
        print("Fizz")

    # check if number is divisible by 5 only
    elif number % 5 == 0:
        print("Buzz")

    # none are true, print the number
    else:
        print(number)