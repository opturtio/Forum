from flask import render_template, request, redirect, session, flash
import database

def create_topic(topic, message):
    alert_message = False
    if topic == "":
        flash("Empty topic, try again!")
        alert_message = True
    if message == "":
        flash("Empty comment, try again!")
        alert_message = True
    if message == " ":
        flash("Space is not a comment, try again!")
        alert_message = True
    if database.check_topic_name(topic):
        flash("This topic was already used, try another!")
        alert_message = True
    return alert_message

def add_comment(message):
    alert_message = False
    if message == "":
        flash("Empty comment, try again!")
        alert_message = True
    if message == " ":
        flash("Space is not a comment, try again!")
        alert_message = True
    return alert_message