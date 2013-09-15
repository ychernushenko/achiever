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
    cursor = conn.execute("SELECT * from goals WHERE owner_id=%s", ownerId)
    return cursor

def getHtmlForOwner(ownerId):
    cursor = getGoalsForOwner(ownerId)
    for record in cursor:
