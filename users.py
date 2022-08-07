from flask import session
from db import db
from werkzeug.security import check_password_hash, generate_password_hash

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
            return True
        else:
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

def check_user(username, password, password2):
    if password != password2:
        return False
    if len(password) < 8:
        return False
    if check_username(username):
        return False
    return True
    
    
def check_username(username):
    sql = "SELECT id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username": username}).fetchone()
    if result:
        return True
    return False