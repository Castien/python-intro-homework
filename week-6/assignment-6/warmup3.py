

# Demonstrate variable scope with two short examples in one file:

# Define a variable inside a function. 
# Try to access it outside the function and show the NameError — paste the error in a comment, 
# then remove or comment out the line that causes it.
# Show how return solves the problem: 
# return the value from the function and assign it to a variable in the outer scope. 
# Print it to confirm it worked.



# Define a variable inside a function:
# def functional_function():
#     does_a_thing = "I do a thing!"
#     print(does_a_thing)

# Try to access it outside the function and show the NameError — paste the error in a comment:
# then remove or comment out the line that causes it.
# functional_function()
# NameError: name 'functional_function' is not defined

# return the value from the function
def functional_function():
    does_a_thing = "I do a thing!"
    return does_a_thing

#  Assign it to a variable in the outer scope.
outer_space = functional_function()

# Print it to confirm it worked.
print(outer_space)