# Open names.txt and read its contents
# append a new name at the end of the file

with open("names.txt", "r") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)

with open("names.txt", "a") as file_object:
    print("Appending new name to the file...")
    file_object.write("Nicole Song\n") #add a \n so the next name will be added on a new line
