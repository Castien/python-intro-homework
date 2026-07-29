

#Create two hardcoded lists of programming languages (some overlap, some unique to each list). 
# Convert each to a set and print: 
# The union (all languages from both lists, no duplicates) 
# The intersection (languages in both lists) 
# The difference (languages only in the first list)

# Two hardcoded lists of programming languages
languages_1 = ["Python", "JavaScript", "Java", "C++", "Ruby"]
languages_2 = ["Python", "JavaScript", "Go", "Rust", "C++"]

# Convert lists to sets
set_1 = set(languages_1)
set_2 = set(languages_2)

# Union - all languages from both sets
print(set_1.union(set_2))

# Intersection - languages in both sets
print(set_1.intersection(set_2))

# Difference - languages only in the first set
print(set_1.difference(set_2))
