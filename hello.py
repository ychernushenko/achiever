import os
import urlparse
from flask import Flask, render_template, send_from_directory, request
from goals import goal
from login import login
from db_connect import insert

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return login()

@app.route('/create', methods=['POST', 'GET'])
def create():
    owner_id = request.form['owner_id']
    uname = request.form['uname']
    details = request.form['details']
    binary=""
    privacy=""
    reminder_date = "01-01-2001"
    creation_date = "15-09-2013"
    print request.form['date']
    dueDate = request.form['date']
    reminder_period = ""
    status = "IN PROGRESS"

    insert(uname, details, dueDate, binary, privacy, reminder_date, reminder_period, creation_date, status, owner_id)
    return goal(owner_id)


@app.route('/<path:filename>.html', methods=['POST', 'GET'])
def channel(filename):
    return send_from_directory('templates', filename+".html")

@app.route('/<userid>', methods=['POST', 'GET'])
def hello(userid):
    return goal(userid)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
