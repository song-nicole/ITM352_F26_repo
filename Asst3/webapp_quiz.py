#Application to manage quiz webapp

#Assignment 3 should have multiple html pages
'''
1. home page
2. quiz questions
3. question result (could be on the same page as the previous one on quiz questions)
4. final results
'''

from flask import Flask, render_template, request, redirect, url_for

#Global variables
score = 0
question_number = 0
questions = [       #Replace with a json file later
    {"question": "What is the capital of France?",
     "options": ["London", "New York", "Tokyo", "Paris"]},
    {"question": "What planet is known as the red planet?",
     "options": ["Venus", "Jupiter", "Saturn", "Mars"]}
]
max_questions = len(questions)

app = Flask(__name__) #__name__ is the name of the program, is the default name

@app.route('/') #AKA index.html
def index():
    global score, question_number
    score = 0
    question_number = 0
    return render_template('index.html')

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    global score, question_number, max_questions, questions
    if request.method == "POST": #POST is when user submits the form
        #Capture the answer from the form
        answer = request.form.get("answer") #'answer' is the name of the radio button assigned in 'quiz.html'
        #Check if the answer is correct
        if answer == questions[question_number]["options"][-1]:
            score += 1
        question_number += 1
    if question_number < max_questions:
        #Render the next question
        return render_template('quiz.html',
                               question=questions[question_number]["question"],
                               question_number=question_number,
                               options=questions[question_number]["options"])
    else:
        #Quiz is over, save the data and return to the results page
        return render_template('results.html', score=score, max_questions=max_questions)

@app.route('/results')
def results():
    #Display the final score
    global score, max_questions
    return render_template('results.html', score=score, max_questions=max_questions)

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
