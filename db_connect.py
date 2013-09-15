import os
import psycopg2
import urlparse

from flask import Flask

app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])


@app.route('/', methods=['POST', 'GET'])
def getGoals():
    print "Connecting to database ..."
    conn = psycopg2.connect(database=url.path[1:], user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM goals")
    for record in cursor:
        print record
        print type(record)
    return cursor


def getGoalsForOwner(ownerId):
    conn = psycopg2.connect(database=url.path[1:], user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
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

