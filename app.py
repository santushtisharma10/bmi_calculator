from flask import Flask, render_template, request

app = Flask(__name__)


def calc( weight, height):
    bmi = weight/(height**2)
    return bmi


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/form", methods={"GET", "POST"})
def form():
    return render_template("form.html")

    if request.form =="POST":


@app.route("/result")
def result():

    return render_template("result.html", weight, height)

if __name__ == "__main__":
    app.run(debug=True)
