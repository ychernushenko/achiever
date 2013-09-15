import os
import psycopg2
import urlparse

from flask import Flask

app = Flask(__name__)

def getGoalsForOwner(ownerId):
    conn = psycopg2.connect(database="ddg1e2pn2rcqt6", user="xazmiyanlmjvcz",
                            password="7e7AgvwcRuoqWszdsTMxYb4edZ",
                            host="ec2-54-225-68-241.compute-1.amazonaws.com",
                            port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT name, details, status from goals WHERE owner_id = %s", (ownerId, ))
    print cursor.rowcount
    return cursor


def getHtmlForGoals(ownerId):
    cursor = getGoalsForOwner(ownerId)
    a = cursor.fetchall()
    f = open("templates/data_replace.html")
    s = ""
    for line in f:
        s += line
    counter = 0
    result = ""
    for r in a:
        result += s % ("mCheck" + str(counter), r[0], 
                      r[1], "mButton" + str(counter), r[2])
        counter += 1
    return result


def getFollowersHtml(ownerId):
    return ""


def getRequestsHtml(ownerId):
    return ""


def getHtml(ownerId):
    r = getHtmlForGoals(ownerId)
    s = getFollowersHtml(ownerId)
    t = getRequestsHtml(ownerId)
    f = open("templates/data_table.html")
    html = ""
    for line in f:
        html += line
    return html % (r, s, t)

