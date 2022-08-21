from flask import render_template, request, redirect, session, url_for
from app import app
import users, database


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        #TODO check if user is logged in
        return render_template("index.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/forum")
        else:
            #TODO here javascript if something went wrong
            return redirect("/")

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
    return redirect("/signup")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/forum")
def forum():
    return render_template("forum.html")

@app.route("/create_topic", methods=["GET", "POST"])
def create_topic():
    if request.method == "GET":
        return render_template("create_topic.html")
    #TODO continue from here to create database for message and topic
    if request.method == "POST":
        topic = request.form["topic"]
        message = request.form["message"] # message have to be inserted to database
        return redirect("/forum", topic=topic, message=message)
    return render_template("create_topic.html")

@app.route("/comments")
def comments():
    topic = request.form["topic"]
    fetched_comments = database.fetch_comments(topic)
    return render_template("comments.html", fetched_comments=fetched_comments)