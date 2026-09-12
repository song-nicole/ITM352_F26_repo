import HandyMath
from HandyMath import max, min

# Get the two numbers that will be used in each HandyMath calculation.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Use the first number for the square-root-of-square calculation and as the base.
square_root_of_square = HandyMath.squareroot(number1 ** 2)
exponent_result = HandyMath.exponent(number1, number2)

# Display all results with f-strings so the values are inserted into readable text.
print(f"The midpoint of {number1} and {number2} is {HandyMath.midpoint(number1, number2)}.")
print(f"The square root of the square of {number1} is {square_root_of_square}.")
print(f"{number1} raised to the exponent {number2} is {exponent_result}.")
print(f"The maximum of {number1} and {number2} is {max(number1, number2)}.")
print(f"The minimum of {number1} and {number2} is {min(number1, number2)}.")
