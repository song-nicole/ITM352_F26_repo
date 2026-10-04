data = ("hello", "10", "goodbye", 3, "goodnight", 5)

string_count = 0

def try_accept_tuples():
    try:
        user =input("Enter a string: ")
        data.append(user)
    except:
        print("An error occurred while trying to append the user input to the data tuple. Tuples are immutable.")

try_accept_tuples()
