#function outputs Hello!
def say_hello():
    print("Hello!")

say_hello()

#function outputs Hello, (name)!
def greet(name):
    print(f"Hello, {name}!")

greet("Nicole")

#function multiplies 2 numbers and returns the result
def add_numbers(first_number, second_number):
    return first_number + second_number

result = add_numbers(5, 3)
print(result)

#default parameter
#used when you want to give a default value to a parameter in case the user does not provide one
def greet_with_title(name, title="Student"):
    print(f"Hello, {title} {name}!")

greet_with_title("Nicole")
greet_with_title("Nicole", "Professor")

#function that conbines the above concepts
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}.")

describe_pet("Max")
describe_pet("Milo", "cat")

#using the return statement
#return statement sends a value from a function back to the code that called it

#returning a number
def add_numbers(first_number, second_number):
    return first_number + second_number

result = add_numbers(5, 3)
print(result)

#returning a string
def create_greeting(name):
    return f"Hello, {name}!"

message = create_greeting("Nicole")
print(message)

#returning a boolean
def is_even(number):
    return number % 2 == 0

answer = is_even(10)
print(answer)

print(is_even(7))

#local vs global scope
#local scope refers to variables that are defined within a function and can only be accessed within that function
#global scope refers to variables that are defined outside of any function and can be accessed from anywhere in the code

#local scope example - price is defined within the function
def calculate_total():
    price = 10
    print(price)

calculate_total()

#global scope example - school is defined outside of the function
school = "University of Hawaii"

def show_school():
    print(school)

show_school()

#changing a global variable within a function can cause issues
#should use the "global" keyword to prevent it
#but recommended to use parameters and return values instead

#causes UnboundedLocalError
count = 0

def increase_count():
    count = count + 1

#using global keyword
count = 0

def increase_count():
    global count
    count += 1

increase_count()
print(count)

#using parameters and return values
def increase_count(count):
    return count + 1

count = 0
count = increase_count(count)

print(count)

#the local variable doesn't change the global variable, when called outside a function
#when called outside a function, the global variable is used and the local variable is ignored

#practical examples of calculating real problems

#calculating area of a rectangle
def rectangle_area(length, width):
    return length * width

area = rectangle_area(10, 5)
print(f"The area is {area} square units.")

#mathematical equations
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    return sum(numbers) / len(numbers)

temperatures = [72, 75, 68, 70]
average = calculate_average(temperatures)

print(f"Average temperature: {average}")

#processing strings
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "Python functions are useful"
print(count_words(sentence))
