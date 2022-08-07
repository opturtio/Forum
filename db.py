from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app

#FIXME replacing postgres for postgresql because SQLAlchemy doesnt support 'postgres' dialect anymore, 
# and heroku doesnt allow to overdrive the DATABASE_URL value (a detach needs to be done. check:
# https://stackoverflow.com/questions/35061914/how-to-change-database-url-for-a-heroku-application)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("postgres", "postgresql")
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username
    
db.create_all()