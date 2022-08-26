from flask import session
from db import db

def insert_topic(topic, user_id):
    sql = "INSERT INTO topics (topic, user_id, created_at) VALUES (:topic, :user_id, NOW())"
    db.session.execute(sql, {"topic":topic, "user_id":user_id})
    db.session.commit()
    return
    

def insert_message(message, topic_id, user_id):
    sql = "INSERT INTO messages (content, topic_id, user_id, created_at) VALUES (:content, :topic_id, :user_id, NOW())"
    db.session.execute(sql, {"content":message, "topic_id":topic_id, "user_id":user_id})
    db.session.commit()
    return

def fetch_topics():
    sql = "SELECT topic, created_at FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def fetch_topic_id(topic):
    sql = "SELECT id FROM topics where topic=:topic"
    result = db.session.execute(sql, {"topic":topic})
    topic_id = result.fetchone()[0]
    return topic_id
    
    

def fetch_comments_by_topic(topic_id):
    sql = "SELECT  FROM messages"
    result = db.session.execute(sql)