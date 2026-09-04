#this program prompts the user to enter a temperature in Farenheight and then converts it to Celcius.
#create the conversion as a function

#Name: Nicole
#Date: Sept. 4, 2026

def F_to_C(farenheight):
    celcius = (farenheight - 32) * 5/9
    rounded_celcius = round(celcius, 2)
    return rounded_celcius

farenheight_input = input("Enter temperature in Farenheight: ")
farenheight_float = float(farenheight_input)

celcius_value = F_to_C(farenheight_float)

print("You entered", farenheight_float)
print("The temperature in Celcius is:", celcius_value)
