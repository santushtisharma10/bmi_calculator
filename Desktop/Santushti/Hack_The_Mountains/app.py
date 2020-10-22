from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def fn():
    req = request.form.getlist('mymultiselect')
    print(req)
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)