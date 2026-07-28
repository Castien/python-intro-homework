

# Ask the user for a number. Using two separate if/elif/else blocks 
# one for sign, one for parity — print two lines of output:
# Enter a number: -7
# -7 is negative.
# -7 is odd.
# Enter a number: 0
# 0 is zero.
# 0 is even.
# Handle 0 as its own sign case (neither positive nor negative).

number = int(input("Enter a number: "))

# Sign: Check if # is positive, negative, or zero.

if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Parity: Check if the number is even or odd.

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")