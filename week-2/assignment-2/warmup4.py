# name = input("What is your name? ")
# print(hello + name)

# 1: Error message
# Castien@Arcadia MINGW64 ~/Desktop/Code the Dream/python-intro-homework/week-2/assignment-2 (assignment-2)
# $ python warmup4.py
# What is your name? Eileen
# Traceback (most recent call last):
#   File "C:\Users\Castien\Desktop\Code the Dream\python-intro-homework\week-2\assignment-2\warmup4.py", line 2, in <module>
#     print(hello + name)
#           ^^^^^
# NameError: name 'hello' is not defined. Did you mean: 'help'?

# 2: What caused it?
# Missing greeting variable, variable undefined.

# 3: How did you fix it?
# Added variable.

name = input("What is your name? ")
greeting = "Hello, "
print(greeting + name)