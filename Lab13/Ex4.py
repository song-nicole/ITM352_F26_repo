#Create a skeleton of your quiz game using flask

from flask import Flask, session, redirect, url_for, render_template_string, request
import json
import random
from pathlib import Path

app = Flask(__name__)
app.secret_key = "quiz-secret-key"

BASE_DIR = Path(__file__).parent.parent / "Assignment1"

with open(BASE_DIR / "questions.json") as file:
    ALL_QUESTIONS = json.load(file)

HTML = """
<!doctype html>
<html>
<head>
    <title>Hawaii Quiz</title>
    <meta charset="UTF-8">
</head>
<body>
    <h1>Hawaii Quiz</h1>

    {% if finished %}
        <h2>You scored {{ score }} out of {{ total }}!</h2>
        <a href="{{ url_for('start') }}">Play again</a>
    {% else %}
        <p>Question {{ number }} of {{ total }}</p>
        <h2>{{ question }}</h2>

        {% if image %}
            <img src="{{ image }}" alt="Question image" width="500">
        {% endif %}

        <p>Current score: {{ score }}</p>

        <form method="post" action="{{ url_for('answer') }}">
            {% for option in options %}
                <p>
                    <label>
                        <input type="radio" name="answer" value="{{ option }}" required>
                        {{ option }}
                    </label>
                </p>
            {% endfor %}

            <button type="submit">Submit answer</button>
        </form>
    {% endif %}
</body>
</html>
"""

@app.route("/")
def home():
    if "questions" not in session:
        return redirect(url_for("start"))

    index = session["index"]

    if index >= len(session["questions"]):
        return render_template_string(
            HTML,
            finished=True,
            score=session["score"],
            total=len(session["questions"]),
        )

    question, data = session["questions"][index]

    if isinstance(data, dict):
        options = data["answers"]
        image = data["image"]
    else:
        options = data
        image = None

    return render_template_string(
        HTML,
        finished=False,
        question=question,
        options=options,
        image=image,
        number=index + 1,
        total=len(session["questions"]),
        score=session["score"],
    )

@app.route("/start")
def start():
    questions = random.sample(
        list(ALL_QUESTIONS.items()),
        min(5, len(ALL_QUESTIONS)),
    )

    session["questions"] = questions
    session["index"] = 0
    session["score"] = 0

    return redirect(url_for("home"))

@app.post("/answer")
def answer():
    index = session["index"]
    question, data = session["questions"][index]

    correct_answer = data["answers"][0] if isinstance(data, dict) else data[0]

    if request.form["answer"] == correct_answer:
        session["score"] += 1

    session["index"] += 1
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)