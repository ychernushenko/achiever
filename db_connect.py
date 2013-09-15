import datetime
import time

import psycopg2
from flask import Flask, jsonify


app = Flask(__name__)


def connect():
    return psycopg2.connect(database="ddg1e2pn2rcqt6", user="xazmiyanlmjvcz",
                            password="7e7AgvwcRuoqWszdsTMxYb4edZ",
                            host="ec2-54-225-68-241.compute-1.amazonaws.com",
                            port="5432")


def getTableTemplate():
    f = open("templates/data_replace.html")
    s = ""
    for line in f:
        s += line
    return s


def getHtmlForGoals(ownerId):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT name, details, status, id from goals WHERE owner_id = %s", (ownerId, ))
    a = cursor.fetchall()
    s = getTableTemplate()
    result = ""
    for r in a:
        result += s % ("mCheck" + str(r[3]), r[0],
                       r[1], "mButton" + str(r[3]), r[2])
    cursor.close()
    conn.close()
    return result


def getFollowersHtml(followerId):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT name, details, status, g.id as g_id FROM goals g INNER JOIN follower_goal f
    ON g.id = f.goal_id WHERE follower_id = %s""", (followerId, ))
    s = getTableTemplate()
    a = cursor.fetchall()
    result = ""
    for r in a:
        result += s % ("mCheck" + str(r[3]), r[0],
                       r[1], "mButton" + str(r[3]), r[2])
    cursor.close()
    conn.close()
    return result


def getRequestsHtml(followerId):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT name, details, status, g.id as g_id x FROM goals g INNER JOIN request_follower r
    ON g.id = r.goal_id WHERE follower_id = %s""", (followerId, ))
    s = getTableTemplate()
    a = cursor.fetchall()
    result = ""
    for r in a:
        result += s % ("mCheck" + str(r[3]), r[0],
                       r[1], "mButton" + str(r[3]), r[2])
    cursor.close()
    conn.close()
    return result


def getJSONObject(query, args=()):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(query, args)
    a = [x for x in cursor]
    #The name is stored at index 0 of the 7-tuple
    b = [x[0] for x in cursor.description]

    result = []
    for row in a:
        res = {}
        for name, y in zip(b, row):
            res[name] = y
        result.append(res)
    connection.close()
    cursor.close()
    return jsonify(*result)


def getHtml(ownerId):
    r = getHtmlForGoals(ownerId)
    s = getFollowersHtml(ownerId)
    t = getRequestsHtml(ownerId)
    f = open("templates/data_table.html")
    html = ""
    for line in f:
        html += line
    return html % (r, s, t)


def insert(name, details, dueDate, binary, privacy, reminder_date,
           reminder_period, status, owner_id):
    conn = connect()
    t = time.strptime(dueDate, "%d-%m-%Y")
    u = time.strptime(reminder_date, "%d-%m-%Y")
    ty = t.tm_year
    tm = t.tm_mon
    td = t.tm_mday
    uy = u.tm_year
    um = u.tm_mon
    ud = u.tm_mday
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO goals (name, details, due_date, picture, privacy, reminder_date, reminder_period,
    creation_date, status, owner_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                   (name, details, datetime.datetime(ty, tm, td), psycopg2.BINARY(binary), privacy,
                    datetime.datetime(uy, um, ud), reminder_period, status, owner_id))
    cursor.close()
    conn.close()