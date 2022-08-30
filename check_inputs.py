from flask import render_template, request, redirect, session, flash
import database

def create_topic(topic, message):
    input = False
    if topic == "":
        flash("Empty topic, try again!")
        input = True
    if message == "":
        flash("Empty comment, try again!")
        input = True
    if message == " ":
        flash("Space is not a comment, try again!")
        input = True
    if database.check_topic_name(topic):
        flash("This topic was already used, try another!")
        input = True
    return input

def add_comment(message):
    input = False
    if message == "":
        flash("Empty comment, try again!")
        input = True
    if message == " ":
        flash("Space is not a comment, try again!")
        input = True
    return input