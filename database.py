from flask import session
from db import db

def fetch_comments(topic):
    sql = "SELECT * FROM messages"
    result = db.session.execute(sql)