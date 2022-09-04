from flask import session
from werkzeug.security import generate_password_hash
from db import db
import check_inputs

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if check_inputs.check_login(username, password, user):
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

def logout():
    del session["user_id"]
    del session["username"]
    del session["csrf_token"]
