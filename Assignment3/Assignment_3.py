#Name: Nicole Song
#Date: November 13, 2026

#Assignment: Turn the quiz game from Assignment 1 into an interactive web application
#Requirement 1 (#1): Use cookies or sessions to check if a user has already visited the quiz game and act accordingly
#Requirement 2 (#5): Allow users to request a hint on a question and limit it to once per game OR deduct points when used

#Started with parts from the Assignment 3 Workshop, parts from Assignment 1, and parts from Lab13 Ex4

from flask import Flask, render_template, request, redirect, url_for
import json
import random

#Access the questions from the JSON file
with open("questions.json") as file:
    ALL_QUESTIONS = json.load(file)

#Global variables
score = 0
question_number = 0
questions = [] #List of questions to be asked each round
hint_used = False

QUESTIONS_PER_QUIZ = 5
num_questions = min(QUESTIONS_PER_QUIZ, len(ALL_QUESTIONS))

app = Flask(__name__)

#index.html
@app.route('/')
def index():
    global score, question_number, questions
    score = 0
    question_number = 0
    questions = random.sample(list(ALL_QUESTIONS.items()), num_questions)
    return render_template('index.html')

#quiz.html
@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global score, question_number, questions

    if request.method == "POST":
        question_data = questions[question_number][1]
        correct_answer = question_data[0]

        if request.form.get("answer") == correct_answer:
            score += 1
        
        question_number += 1

    if question_number >= len(questions):
        return render_template("results.html", score = score, num_questions = num_questions)

    question_data = questions[question_number][1]

    #Randomize the options for each question
    options = list(question_data)
    random.shuffle(options)

    return render_template("quiz.html",
        question_number = question_number, question = questions[question_number][0],
        options = options, score = score, num_questions = num_questions)

#results.html
@app.route('/results', methods=["GET", "POST"])
def results():
    global score, num_questions
    return render_template('results.html', score = score, num_questions = num_questions)
    

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
