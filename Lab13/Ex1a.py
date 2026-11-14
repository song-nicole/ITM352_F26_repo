#Flask is installed locally (within the python file) and should be accessed locally

#enter: "python3 -m flask --app Ex1a run --debug" to enter debug mode and run flask
#control + c to end flask

#Test flask with this
from flask import Flask
app = Flask(__name__) #Runs the flask function -> will keep running and automatically updates when you resave your code

@app.route('/')
def hello():
    return '<strong>Hello</strong> World!' #By default, it will be processed as html or plain text
