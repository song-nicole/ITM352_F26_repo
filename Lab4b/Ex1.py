#Properly format an inputted name in title case

#orignial input
raw_name = input("Enter a name: ")

#formatting the input
stripped_name = raw_name.strip()
title_case_name = stripped_name.title()
print("Formatted name in title case: ", title_case_name)
