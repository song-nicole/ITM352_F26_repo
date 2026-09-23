#Learning about dictionaries with Copilot

#Each dictionary stores data in key-value pairs
#Each key is used to find its corresponding value

#Format of a dictionary
dictionary_name = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",}

#access a value using the key
value = dictionary_name["key1"]

#access a value with get()
value = dictionary_name.get("key1")

#add a new key-value pair to the dictionary
dictionary_name["key4"] = "value4"

#update an exisiting value
dictionary_name["key1"] = "1"

# pdate() adds or changes multiple items
dictionary_name.update({
    "key5" : "value5",
    "key6" : "value6"
})

#remove a key-value pair from the dictionary
dictionary_name.pop("key4")
dictionary_name.popitem() #removes last key-value pair

#deleting all items from the dictionary
dictionary_name.clear()

#getting all keys
dictionary_name.keys()

#getting all values
dictionary_name.values()

#getting all key-value pairs
dictionary_name.items()

#to loop through a dictionary
for key, value in dictionary_name.items():
    print(key, "is ", value)


#Nested dictionaries
#A dictionary containing another dictionary and a list
student = {
    "name": "Nicole",
    "contact": {
        "email": "nicole@example.com",
        "phone": "555-1234"
    },
    "classes": ["ITM 352", "Accounting"]
}

#Access a regular value
print(student["name"])

#Access a value inside a nested dictionary
print(student["contact"]["email"])

#Access an item in a list
print(student["classes"][0])