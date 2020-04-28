from flask import Flask, render_template, request, session
from flask_session import Session

errorr = "Incorrect Name. Please enter your correct full name Sinsin."

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SECRET_KEY"] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Session(app)

@app.route("/")
def index():
    return render_template("index.html", errorr = "")

@app.route("/hello", methods=["POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("name")
        if name != "Swati Sinsinwar":
            return render_template("index.html", errorr = errorr)
        else:
            return render_template("list.html", notes = session['notes'])



@app.route("/list", methods=["GET", "POST"])
def list():
    if len(session.get('notes')) == 0:
        session['notes'] = []
    if request.method == "POST":
        note = request.form.get("note")
        session['notes'].append(note)

    return render_template("list.html", notes = session["notes"])
