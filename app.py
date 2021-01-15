from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    value = " "
    return render_template("imdb.html", value=value)


@app.route("/", methods=["POST"])
def my_form_post():
    s_length_value = request.form["s_length"]
    return render_template("imdb.html", value=s_length_value)


if __name__ == "__main__":
    app.run(debug=True)