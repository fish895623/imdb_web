from flask import Flask, request, render_template
from imdb_learn import learning_imdb

app = Flask(__name__)


@app.route("/")
def index():
    value = " "
    return render_template("imdb.html", value=value)


@app.route("/", methods=["POST"])
def my_form_post():
    imdb_input = request.form["imdb_input"]
    imdb_input = learning_imdb().sentiment_predict(imdb_input)
    return render_template("imdb.html", value=imdb_input)


if __name__ == "__main__":
    app.run(debug=True)