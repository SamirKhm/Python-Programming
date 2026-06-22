from flask import Flask,jsonify

app = Flask(__name__)



@app.route("/")
def hello_world():
    marks={
    "harry":36,
    "Rohan":59,
    "Shubham":100
}
    return jsonify(marks)

app.run(debug=True)