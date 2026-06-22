from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    marks = {
        "John": 85,
        "Alice": 90,
        "Bob": 78,
        "Eve": 92,
        "Charlie": 88,
        "David": 100
    }
    return render_template("index.html", marks=marks)

if __name__ == "__main__":
    app.run(port=8000, debug=True)