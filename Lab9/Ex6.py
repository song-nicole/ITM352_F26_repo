# Read a file of quiz questions and save as a dictionary
import json

filename = "quiz_questions.json" #path to the json file
with open(filename, 'r') as file:
    questions = json.load(file) #load the JSON object from the file into a dictionary

print(questions)