data = ("hello", "10", "goodbye", 3, "goodnight", 5)

string_count = 0

'''
def try_accept_tuples():
    global data
    try:
        user = input("Enter a string: ")
        data.append(user)
    except:
        data = data + (user,)
        print(data)

try_accept_tuples()
'''

#Using the unpacking operator
'''
def try_accept_tuples():
    global data
    try:
        user = input("Enter a string: ")
        data.append(user)
    except:
        data = (*data, user)
        print(data)

try_accept_tuples()
'''

#convert the tuple to a list, add the user input, and convert it back to a tuple
def try_accept_tuples():
    global data
    try:
        data_list = list(data)
        data_list.append(user)
        data = tuple(data_list)
    except:
        user = input("Enter a string: ")
        data_list = list(data)
        data_list.append(user)
        data = tuple(data_list)
        print(data)

try_accept_tuples()