from db import db

def users():
    sql = "SELECT COUNT(id) FROM users"
    result = db.session.execute(sql)
    users = result.fetchone()[0]
    return users

def topics():
    sql = "SELECT COUNT(id) FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchone()[0]
    return topics

def comments():
    sql = "SELECT COUNT(id) FROM messages"
    result = db.session.execute(sql)
    comments = result.fetchone()[0]
    return comments

