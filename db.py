from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app

#FIXME replacing postgres for postgresql because SQLAlchemy doesnt support 'postgres' dialect anymore, 
# and heroku doesnt allow to overdrive the DATABASE_URL value (a detach needs to be done. check:
# https://stackoverflow.com/questions/35061914/how-to-change-database-url-for-a-heroku-application)

#For heroku:
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("postgres", "postgresql")

#For local:
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)
