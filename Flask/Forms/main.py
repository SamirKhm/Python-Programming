from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def hello_world():
    if(request.method=="POST"):
        #Handle the form data here
        with open("file.txt","w") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']}\n")
        return "Form submitted successfully"
    else:
        return render_template("contact.html")

app.run(port=8000,debug=True)