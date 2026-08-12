

# Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways:
# With only a name argument
# With both a name and a custom greeting
# With the greeting passed as a keyword argument
# Expected output:

# Hello, Alex!
# Good morning, Alex!
# Hello, Alex!

# Write a function greet(name, greeting="Hello") that prints a greeting.
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# With only a name argument
greet("Alex")

# With both a name and a custom greeting
greet("Alex", "Good morning")

# With the greeting passed as a keyword argument
greet("Alex", greeting="Hello")