'''
Prompt co-pilot to create a function that converts temperatures
 to and from celsius, fahrenheit, and kelvin. 
 The function should take as an argument a conversion function 
 rather than ask the user what conversion to make.
'''

#Name: Nicole Song
#Date: Sept. 11. 2026

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature(temperature, conversion_function):
    return conversion_function(temperature)