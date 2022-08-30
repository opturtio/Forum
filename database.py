from flask import session
from db import db

def insert_topic(topic, user_id, posts):
    sql = "INSERT INTO topics (topic, user_id, posts, created_at) VALUES (:topic, :user_id, :posts, NOW())"
    db.session.execute(sql, {"topic":topic, "user_id":user_id, "posts":posts})
    db.session.commit()
    return
    
def insert_message(message, topic_id, user_id):
    sql = "INSERT INTO messages (content, topic_id, user_id, created_at) VALUES (:content, :topic_id, :user_id, NOW())"
    db.session.execute(sql, {"content":message, "topic_id":topic_id, "user_id":user_id})
    db.session.commit()
    return

def fetch_topics():
    sql = "SELECT id, topic, posts, created_at FROM topics"
    result = db.session.execute(sql)
    topics = result.fetchall()
    return topics

def fetch_topic_id(topic):
    sql = "SELECT id FROM topics WHERE topic=:topic"
    result = db.session.execute(sql, {"topic":topic})
    topic_id = result.fetchone()[0]
    return topic_id

def fetch_comments_by_topic(topic_id):
    sql = "SELECT content FROM messages WHERE topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id":topic_id})
    comments = result.fetchall()
    return comments

def fetch_number_of_posts(topic_id):
    sql = "SELECT count(*) FROM messages WHERE topic_id=:topic_id"
    result = db.session.execute(sql, {"topic_id":topic_id})
    posts = result.fetchone()[0]
    return posts

def update_number_of_posts(topic_id):
    sql = "UPDATE topics SET posts=posts+1 WHERE id=:topic_id" #FIXME posts doesnt increace
    db.session.execute(sql, {"topic_id":topic_id})
    return