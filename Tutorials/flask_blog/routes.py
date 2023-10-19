from flask import render_template, url_for
from main import app
from forms import RegistrationForm

posts = [
    {
        'author': 'Paing',
        'title': 'Post 1',
        'content': 'First post testing content',
        'date_posted': 'Oct 19,2023'
    },
    {
        'author': 'Zee',
        'title': 'Post 2',
        'content': 'Second post testing content',
        'date_posted': 'Oct 20,2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/login")
def login():
    return "Login"

@app.route("/register")
def register():
    return "Register"