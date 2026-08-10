# Warmup 3: Linear Search
# Start with a hardcoded list of names. Ask the user to enter a name. 
# Loop through the list and print whether the name was found and at what index — or "Not found" if it isn't in the list:

# Enter a name to search for: Marcus
# Found "Marcus" at index 3.
# Enter a name to search for: Zara
# "Zara" was not found in the list.
# Do not use Python's .index() method or the in operator — implement the search yourself with a loop.

# list of names to search
names = ["Pikachu", "Squirtle", "Charmander", "Bulbasaur", "Jigglypuff", "Magikarp"]

# user input for name to search for
search_name = input("Enter a name to search for: ")

# variable to keep track of found status during check
found = False

# loop for index position in the list
for i in range(len(names)):
    # check if the current name matches user input
    if names[i] == search_name:
        print(f'Found "{search_name}" at index {i}.')
        
        # change boolean  to true if name found
        found = True
        
        # end loop if found is true
        break

# loop finishes without finding the name, print statement
if not found:
    print(f'"{search_name}" was not found in the list.')