year = int(input("Enter a year: "))

#Conditional expression
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Function
def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")

is_leap_year(year)