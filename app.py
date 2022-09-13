from flask import Flask, request, render_template
from imdb_learn import learning_imdb

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/imdb")
def imdb():
    value = " "
    return render_template("imdb.html", value=value)


@app.route("/imdb", methods=["POST"])
def my_form_post():
    imdb_input = request.form["imdb_input"]
    result = learning_imdb().sentiment_predict(imdb_input)
    return render_template("imdb.html", result=result, imdb_input=imdb_input)


if __name__ == "__main__":
    app.run()
