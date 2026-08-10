

# Create a hardcoded list of 8 numbers. 
# Without using any loops, print: 
# The first item 
# The last item (use a negative index) 
# A slice containing only the middle four items 
# The full list in reverse order 
# Example output (your numbers will differ): 
# First: 42 
# Last: 40 
# Middle: [83, 5, 61, 29] 
# Reversed: [40, 86, 22, 59, 3, 78, 47, 14]

numbers = [14, 47, 78, 3, 59, 22, 86, 40]

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Middle:", numbers[2:6])
print("Reversed:", numbers[::-1])

# First: 14
# Last: 40
# Middle: [78, 3, 59, 22]
# Reversed: [40, 86, 22, 59, 3, 78, 47, 14]