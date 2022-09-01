from db import db

def users_amount():
    sql = "SELECT COUNT(id) FROM users"
    result = db.session.execute(sql)
    users = result.fetchone()[0]
    return users

def usernames():
    sql = "SELECT username FROM users"
    result = db.session.execute(sql)
    usernames = result.fetchall()
    return usernames

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

def visitors():
    sql = "SELECT count(id) FROM visitors"
    result = db.session.execute(sql)
    visitors = result.fetchone()[0]
    return visitors