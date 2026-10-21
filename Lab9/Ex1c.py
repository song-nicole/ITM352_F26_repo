# Open a file and read its contents

with open("names.txt", "r") as file_object:
    contents = file_object.read()
    print(contents) #Printed as one long string
    contents_list = contents.split("\n")
    print(f"Number of names: {len(contents_list)}")
    for name in contents_list:
        print(name) #Printed as individual names on separate lines as a list