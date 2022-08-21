import secrets
from flask import session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["username"] = username
            session["csrf_token"] = secrets.token_hex(16)
            return True
        return False

def signup(username, password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    except:
        return False
    return

def check_signup_form(username, password, password2):
    if password != password2:
        flash("Those passwords did not match. Try again.")
        return False
    if len(password) < 8:
        flash("Password is too short.")
        return False
    if check_username(username):
        flash("That username is taken. Try another.")
        return False
    return True

def check_username(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username}).fetchone()
    if result:
        return True
    return False

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]
    return
