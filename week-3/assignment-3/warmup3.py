

# Write a script that evaluates the five expressions below and prints each one with its result. 
# Add a comment on each line explaining why the result is what it is:
# print(not True and False)
# print(True or False and False)
# print(not (5 > 3))
# print(10 == 10 and 4 != 4)
# print(not False or not True)

# Precedence: not > and > or - Represented in ().

print(not True and False) # False - not True is False; False and False is False

print(True or False and False) # True - (False and False) (precendence) is (False); True or (False) is True

print(not (5 > 3)) # False - 5 > 3 is True; not True is False

print(10 == 10 and 4 != 4) # False - 10 == 10 is True; 4 != 4 is False; True and False is False

print(not False or not True) # True - not False is True; not True is False; True or False is True


