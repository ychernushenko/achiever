import os
import psycopg2
import urlparse

from flask import Flask

app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

def getGoalsForOwner(ownerId):
    conn = psycopg2.connect(database="ddg1e2pn2rcqt6", user="xazmiyanlmjvcz",
                            password="7e7AgvwcRuoqWszdsTMxYb4edZ",
                            host="ec2-54-225-68-241.compute-1.amazonaws.com",
                            port="5432")
    cursor = conn.execute("SELECT (name, details, status) from goals WHERE owner_id=%s", ownerId)
    return cursor


def getHtmlForGoals(ownerId):
    cursor = getGoalsForOwner(ownerId)
    f = open("templates/data_replace.html")
    s = ""
    for line in f:
        s += line
    counter = 0
    for record in cursor:
        x, y, z = record
        s += f % ("mCheck" + str(counter), y, x, z, "mButton" + str(counter))
        counter += 1
    return s


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

