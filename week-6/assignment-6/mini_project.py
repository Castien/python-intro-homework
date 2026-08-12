
# Open your mini_project.py from Assignment 5. 
# You're going to refactor it so that each operation lives in its own function.

# Create a new file (don't modify your Week 5 submission). 
# Pull a copy of the numbers list from week-5/data/numbers.py into your new script.

# Define the following functions, each taking numbers (a list) as a parameter:
# find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
# find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
# search(numbers, target) — returns the index of target, or -1 if not found
# bubble_sort(numbers) — returns a new sorted list (do not modify the original)
# show_menu() — prints the menu options and returns the user's choice as a string
# main() — the while loop that calls show_menu() and dispatches to the right function
# Call main() at the bottom of the file.

# Requirements:
# No logic should live outside of a function (except the numbers list definition and the main() call)
# bubble_sort should return a new list, not sort in place
# Your search function should print "Found at index X" or "Not found" from inside main(), 
# not inside search() itself — search just returns the index



# list from numbers.py
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
def find_min(numbers):
    # first number is starting smallest value
    minimum = numbers[0]

    # loops to check through every number in the list
    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum


# find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
def find_max(numbers):
    # first number is starting largest value
    maximum = numbers[0]
    # loops to check through every number in the list
    for number in numbers:
        if number > maximum:
            maximum = number

    return maximum


# search(numbers, target) — returns the index of target, or -1 if not found
def search(numbers, target):
    # loops to check each index in list for number
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    # returns -1 if loop fails to find number
    return -1


# bubble_sort(numbers) — returns a new sorted list (do not modify the original)
def bubble_sort(numbers):
    # make copy of numbers list and store in sorted_num list
    sorted_num = numbers[:]

    # repeats until all index positions have been swapped
    while True:
        swapped = False

        # compares pair of numbers next to eachother
        for i in range(len(sorted_num) - 1):
            # swap if the first number is bigger than the second
            if sorted_num[i] > sorted_num[i + 1]:
                temp = sorted_num[i]
                sorted_num[i] = sorted_num[i + 1]
                sorted_num[i + 1] = temp

                # if swapped, switches to true, loops again
                swapped = True

        # if none were swapped, ends loop and returns the sorted_num list
        if not swapped:
            break

    return sorted_num

# show_menu() — prints the menu options and returns the user's choice as a string
def show_menu():
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    return choice


# main() — the while loop that calls show_menu() and dispatches to the right function
def main():
    # loops menu until the user chooses Quit
    while True:
        choice = show_menu()

        # Find minimum
        if choice == "1":
            minimum = find_min(numbers)
            print(f"Minimum value: {minimum}")

        # Find maximum
        elif choice == "2":
            maximum = find_max(numbers)
            print(f"Maximum value: {maximum}")


# Your search function should print "Found at index X" or "Not found" from inside main(),
# not inside search() itself — search just returns the index

        # Search — ask the user for a number and call the search function
        elif choice == "3":
            search_num = int(input("Enter a number to search for: "))

            index = search(numbers, search_num)

            # prints if loop finds the number
            if index != -1:
                print(f"Found at index {index}")

            # prints if loop fails to find number
            else:
                print("Not found")

        # Sort — call bubble_sort and prints new sorted list
        elif choice == "4":
            sorted_num = bubble_sort(numbers)
            print(f"Sorted list: {sorted_num}")

        # Quit — print a message and exits the loop.
        elif choice == "5":
            print("Goodbye!")
            break

        # if user inputs invalid menu option
        else:
            print("Invalid option. Please choose 1-5.")


# Call main() at the bottom of the file.
main()


# Run test results, without the repeated menu:

# === Number Cruncher ===
# 1. Find minimum
# 2. Find maximum
# 3. Search for a number
# 4. Sort the list
# 5. Quit

# Choose an option (1-5): 1
# Minimum value: 3

# Choose an option (1-5): 2
# Maximum value: 93

# Choose an option (1-5): 3
# Enter a number to search for: 50
# Not found

# Choose an option (1-5): 3
# Enter a number to search for: 8
# Found at index 7

# Choose an option (1-5): 4
# Sorted list: [3, 5, 8, 14, 17, 22, 29, 31, 40, 42, 47, 55, 59, 61, 66, 74, 78, 83, 86, 93]

# Choose an option (1-5): 6
# Invalid option. Please choose 1-5.

# Choose an option (1-5): 5
# Goodbye!


