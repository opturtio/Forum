from flask import session
from db import db
from statistics import comments

def insert_visitor(username):
    sql = "INSERT INTO visitors (username, time) VALUES (:username, NOW())"
    db.session.execute(sql, {"username":username})
    db.session.commit()
    return

def check_topic_name(topic):
    sql = "SELECT COUNT(*) FROM topics WHERE topic=:topic"
    result = db.session.execute(sql, {"topic":topic})
    amount = result.fetchone()[0]
    if amount > 0:
        return True
    return False

def insert_topic(topic, user_id, posts):
    sql = "INSERT INTO topics (topic, user_id, posts, created_at) VALUES (:topic, :user_id, :posts, NOW())"
    db.session.execute(sql, {"topic":topic, "user_id":user_id, "posts":posts})
    db.session.commit()
    return
    
def insert_message(message, topic_id, user_id, username):
    sql = "INSERT INTO messages (content, topic_id, user_id, username, created_at) VALUES (:content, :topic_id, :user_id, :username, NOW())"
    db.session.execute(sql, {"content":message, "topic_id":topic_id, "user_id":user_id, "username":username})
    db.session.commit()
    return

def fetch_topics():
    sql = "SELECT t.*, count(m.id) as posts FROM topics t INNER JOIN messages m ON t.id = m.topic_id GROUP BY t.id;"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def fetch_topic_id(topic):
    sql = "SELECT id FROM topics WHERE topic=:topic"
    result = db.session.execute(sql, {"topic":topic})
    topic_id = result.fetchone()[0]
    return topic_id

def fetch_comments_by_topic(topic_id):
    sql = "SELECT username, created_at, content FROM messages WHERE topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id":topic_id})
    comments = result.fetchall()
    return comments

def fetch_number_of_posts(topic_id):
    sql = "SELECT count(*) FROM messages WHERE topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id":topic_id})
    posts = result.fetchone()[0]
    return posts

def search(query):
    sql = "SELECT content, username, created_at FROM messages m WHERE content LIKE :query"
    #sql = "SELECT topics.topic, messages.content, messages.username, messages.created_at FROM messages JOIN topics ON content LIKE :query AND m.topic_id=t.id GROUP BY t.id"
    result = db.session.execute(sql, {"query": "%"+query+"%"})
    comments = result.fetchall()
    return comments
