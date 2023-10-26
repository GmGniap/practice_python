from flask import render_template, url_for, flash, redirect, request, jsonify
from blog import app, db
from blog.forms import RegistrationForm
from blog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import json

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

@app.route('/child')
def child():
    user = {'username': 'Paing'}
    return render_template('child.html', utc_dt= datetime.datetime.utcnow())

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(fullname=form.fullname.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created! You are now able to log in", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Form', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == "POST":
        check = request.is_json
        print(check)
        email = request.form.get("email")
        password = request.form.get("password")
    
        ## Validation process will be here
    
        user = User.query.filter_by(email=email).first()
        if user and (user.password == password):
            login_user(user, remember=False)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful.')
    return render_template('login.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/profile")
@login_required
def profile():
    image_file = url_for('static', filename='profile_pics/'+ current_user.img_file)
    return render_template("profile.html", title="Profile", image_file=image_file)