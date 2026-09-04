#this program prompts the user to enter a temperature in Farenheight and then converts it to Celcius.

#Name: Nicole
#Date: Sept. 4, 2026

farenheight_input = input("Enter temperature in Farenheight: ")
farenheight_float = float(farenheight_input)

celcius_value = (farenheight_float - 32) * 5/9

celcius_value = round(celcius_value, 2)

print("You entered", farenheight_float)
print("The temperature in Celcius is:", celcius_value)
