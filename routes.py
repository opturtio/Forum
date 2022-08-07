from flask import render_template, request, redirect, session
from app import app
import users


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        #todo check if user is
        return render_template("index.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return render_template("forum.html")
        else:
            #here javascript if something went wrong
            return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]

        if users.check_user(username, password, password2):
            users.signup(username, password)
            return redirect("/")
    return render_template("signup.html")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/forum")
def dashboard():
    return render_template("forum.html")