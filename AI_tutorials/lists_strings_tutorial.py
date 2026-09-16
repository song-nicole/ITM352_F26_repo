#Learning lists and strings with Copilot

movies = ["Frozen", "How to train your dragon", "The lion king", "The incredibles", "Finding nemo"]
print(movies)
movies.append("The little mermaid")
print(movies)
movies.insert(1, "Moana")
print(movies)
movies.remove("The lion king")
print(movies)
movies.pop()
print(movies)
movies.pop(2)
print(movies)
movies.reverse()
print(movies)

print(movies[2]) #prints third element of the list

print(movies[0:3]) #prints first, second and third elements of the list
print(movies[:3]) #prints first, second and third elements of the list
print(movies[::2]) #prints every other element of the list
print(movies[1:4:2]) #prints elements from index 1 to 4 while skipping every other element

string = "This is a sentence"
print(string.split()) #seperates each word into a list item
print(string.find("sentence")) #returns the index where the word is present
print("a" in string) #checks if "a" is in string

print(", ".join(movies)) #joins the list items into a string with ", " in between
