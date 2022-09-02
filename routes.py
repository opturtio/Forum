from tracemalloc import Statistic
from flask import render_template, request, redirect, session, flash, url_for
from app import app
import users, database, check_inputs, statistics as stats


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        #TODO check if user is logged in
        return render_template("index.html")
    
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            database.insert_visitor(username)
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

        if users.check_signup_form(username, password, password2):
            users.signup(username, password)
            return redirect("/")
    return redirect("/signup")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/forum")
def forum():
    if request.method == "GET":
        topics = database.fetch_topics()
        username = session["username"]
        return render_template("forum.html", topics=topics, username=username)

@app.route("/create_topic", methods=["GET", "POST"])
def create_topic():
    if request.method == "GET":
        return render_template("create_topic.html")
    
    if request.method == "POST":
        topic = request.form["topic"] 
        message = request.form["message"]
        user_id = session["user_id"]
        username = session["username"]

        if check_inputs.create_topic(topic, message):
            return render_template("create_topic.html")
        database.insert_topic(topic, user_id)
        topic_id = database.fetch_topic_id(topic)
        database.insert_message(message, topic_id, user_id, username)
        return redirect("/forum")
    return render_template("create_topic.html")

@app.route("/topic/<topic_id>")
def view_topic(topic_id):
    comments = database.fetch_comments_by_topic(topic_id)
    return render_template("comments.html", comments=comments, topic_id=topic_id)

#TODO create delete topic
@app.route("/delete")
def delete_topic():
    return redirect("/forum")

@app.route("/add_comment", methods=["GET", "POST"])
def add_comment():
    if request.method == "POST":
        message = request.form["message"]
        topic_id = request.form["topic_id"]
        user_id = session["user_id"]
        username = session["username"]
        
    if check_inputs.add_comment(message):
        comments = database.fetch_comments_by_topic(topic_id)
        render_template("comments.html", comments=comments, topic_id=topic_id)
    else:
        database.insert_message(message, topic_id, user_id, username)
    comments = database.fetch_comments_by_topic(topic_id)
    return render_template("comments.html", comments=comments, topic_id=topic_id)

@app.route("/search")
def search():
    query = request.args["query"]
    comments = database.search(query)
    return render_template("search.html", comments=comments)
    
@app.route("/statistics")
def statistics():
    amount_of_users = stats.users_amount()
    usernames = stats.usernames()
    amount_of_topics = stats.topics()
    amount_of_comments = stats.comments()
    amount_of_visitors = stats.visitors()
    return render_template("statistics.html", amount_of_users=amount_of_users,
                           usernames=usernames, 
                           amount_of_topics=amount_of_topics, 
                           amount_of_comments=amount_of_comments,
                           amount_of_visitors=amount_of_visitors)
