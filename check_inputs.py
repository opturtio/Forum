from flask import session, flash
from db import db
import database
import secrets
from werkzeug.security import check_password_hash

def create_topic(topic, message):
    alert_message = False
    if topic == "":
        flash("Empty topic, try again!")
        alert_message = True
    if message == "":
        flash("Empty comment, try again!")
        alert_message = True
    if message == " ":
        flash("Space is not a comment, try again!")
        alert_message = True
    if database.check_topic_name(topic):
        flash("This topic was already used, try another!")
        alert_message = True
    return alert_message

def add_comment(message):
    alert_message = False
    if message == "":
        flash("Empty comment, try again!")
        alert_message = True
    if message == " ":
        flash("Space is not a comment, try again!")
        alert_message = True
    return alert_message

def check_login(username, password, user):
    if username == "" or username == " ":
        flash("Username can't be blank")
        return False
    if password == "" or password == " ":
        flash("Password can't be blank")
        return False       
    if not user:
        flash(f"There is no user {username}")
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return True
        flash("Wrong password, try again!")
        return False
    
def check_signup_form(username, password, password2):
    alert_message = False
    if username == "" or username == " ":
        flash("Username too short.")
        alert_message = True
    if password != password2:
        flash("Passwords did not match.")
        alert_message = True
    if len(password) < 8:
        flash("Password is too short.")
        alert_message = True
    if check_username(username):
        flash("That username is taken.")
        alert_message = True
    return alert_message

def check_username(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username}).fetchone()
    if result:
        return True
    return False