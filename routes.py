from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from app import app


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///user"
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():    
    return render_template("signup.html")

