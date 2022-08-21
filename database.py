from flask import session
from db import db

def insert_topic(topic):
    sql = "INSERT INTO topics (topic, created_at) VALUES (:topic, NOW())"
    db.session.execute(sql, {"topic":topic})
    db.session.commit()
    return
    

def insert_message(message):
    sql = "INSERT INTO messages (content, created_at) VALUES (:content, NOW())"
    db.session.execute(sql, {"content":message})
    db.session.commit()
    return

#def fetch_comments(topic):
#    sql = "SELECT * FROM messages"
#    result = db.session.execute(sql)