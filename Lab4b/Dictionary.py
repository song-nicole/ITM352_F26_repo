#Simple dictionary example
#Used for more complicated data structures

'''
dictionary name = {
    key1: value1,
    key2: value2,
    key3: value3,}
'''

country_capitals = {
    "Germany": {"capital": "Berlin", "population": 84000000},
    "Canada": {"capital": "Ottawa", "population": 40000000},
    "France": {"capital": "Paris", "population": 68000000},
}

print("Country capitals: ", country_capitals)
print(country_capitals["Canada"]["capital"])

country_capitals["England"] = {"capital": "London", "population": 58000000}
print(country_capitals["England"]["capital"])

#Checks if key is or is not in dictionary
print("Germany" in country_capitals)
print("Spain" not in country_capitals)