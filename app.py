from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/greet", methods=['GET','POST'])
def greet(name=None):
    if request.method == "POST":
        name = request.form['Username']
        return f"<h1>Hi there, {name}!</h1>"
    elif name==None:
        return "<h1>Hello from the App!</h1>"