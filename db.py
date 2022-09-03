from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app import app

#For heroku:
#app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL").replace("postgres", "postgresql")

#For local:
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)
