#Ask the user to enter a decimat number, calculate the square of that number, round it to 2 decimal places, and print it out

#Name: Nicole Song
#Date: Sept. 2, 2026

input_value = input("Enter a floating point number between 1 and 100: ")
float_value = float(input_value)
squareed_value = float_value ** 2
rounded_value = round(squareed_value, 2)

print("You entered: ", float_value)
print("The square of the number you entered is: ", rounded_value)
