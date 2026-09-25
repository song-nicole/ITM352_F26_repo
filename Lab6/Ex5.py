#Testing the use of assertions
#If the condition is ever false, the program will end with a bug report
#will be used periodically and in ITM 354

def celcius_to_farenheight(celcius):
    assert celcius >= -273.15, "Temperature cannot be below absolute zero"
    farenheight = (celcius * 9/5) + 32
    return farenheight

print(celcius_to_farenheight(0))
print(celcius_to_farenheight(100))
print(celcius_to_farenheight(-300))  # This will trigger the assertion
