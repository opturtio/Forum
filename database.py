from flask import session
from db import db

def fetch_comments(topic):
    sql = "SELECT * from messages"
    result = db.session.execute(sql)