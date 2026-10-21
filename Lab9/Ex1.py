# Open a file of names and print its type

file_object = open("names.txt", "r")
# writing the file (w) is destructive - overwrites the information in the file
# appending to the file (a) adds to the end of the file

print(type(file_object))
file_object.close()