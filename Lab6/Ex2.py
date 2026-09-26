#Write Python code that creates a list with a variety of different values. 
# Include control logic (if, elif, else) that will print different messages whether the list 
# contains fewer than 5 elements, between 5 and 10 (inclusive), and more than 10 elements. 
# Test your code on lists with several different lengths.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if len(my_list) < 5:
    print("The list contains fewer than 5 elements.")
elif 5 <= len(my_list) <= 10:
    print("The list contains between 5 and 10 elements.")
else:
    print("The list contains more than 10 elements.")


test_cases = [
    [1, 2, 3, 4],                         # Fewer than 5
    [1, 2, 3, 4, 5],                      # Exactly 5
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],      # Exactly 10
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # More than 10
]

for my_list in test_cases:
    if len(my_list) < 5:
        print("The list contains fewer than 5 elements.")
    elif 5 <= len(my_list) <= 10:
        print("The list contains between 5 and 10 elements.")
    else:
        print("The list contains more than 10 elements.")