from flask import Flask,render_template,flash

app = Flask(__name__)
app.secret_key="12345"
@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been log out !","success")
    return render_template("index.html")

app.run(debug=True)