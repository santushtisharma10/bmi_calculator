from flask import Flask, render_template, request

app = Flask(__name__)


def calc(weight, height):
    bmi = weight/(height*height)
    return bmi


def checkHealth(bmi):
    if bmi < 18.5:
        status = "underweight"
    elif bmi < 25:
        status = "healthy"
    elif bmi < 30:
        status = "overweight"
    else:
        status = "obese"

    return status


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/form")
def form():
    return render_template("form.html")


@app.route("/form", methods={"GET", "POST"})
def result():
    wt = float(request.form["wt"])
    ht = float(request.form["ht"])
    print(ht, wt)
    bmi = calc(wt, ht)
    status = checkHealth(bmi)
    print(bmi, status)
    return render_template("form.html")
    


if __name__ == "__main__":
    app.run(debug=True)
