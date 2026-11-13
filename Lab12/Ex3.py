from flask import Flask, render_template_string
import requests

app = Flask(__name__)

URL = "https://meme-api.com/gimme/wholesomememes"

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Memes'R'Us</title>
    <meta charset="UTF-8" name="viewport"
          content="width=device-width, initial-scale=0.8">
    <meta http-equiv="refresh"
          content="10; url=http://127.0.0.1:5000">
</head>
<body>
    <h1>Memes'R'Us</h1>
    <img src="{{ meme_url }}" alt="Wholesome meme" width="500">
    <p>Source: r/{{ subreddit }}</p>
</body>
</html>
"""


@app.route("/")
def home():
    response = requests.request("GET", URL)
    response.raise_for_status()

    meme = response.json()
    return render_template_string(
        HTML,
        meme_url=meme["url"],
        subreddit=meme["subreddit"],
    )


if __name__ == "__main__":
    app.run(debug=True)