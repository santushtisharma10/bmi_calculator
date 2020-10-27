from flask import Flask, render_template

app = Flask(__name__)

def calc():
    bmi = weight/(height**2)
    return bmi

def checkHealth():

@app.route("/")
def main():
    return render_template("index.html")
  
@app.route("/form", method={"GET", "POST"})
def form():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)