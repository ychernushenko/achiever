import os
import psycopg2
import urlparse
from flask import Flask

app = Flask(__name__)

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

@app.route('/')
def hello():
    print 3
    db = psycopg2.connect(host="ec2-54-225-68-241.compute-1.amazonaws.com",
                         user="xazmiyanlmjvcz",
                         passwd="7e7AgvwcRuoqWszdsTMxYb4edZ",
                         db="ddg1e2pn2rcqt6")
    print 4
    cur = db.cursor()
    cur.execute("SELECT * FROM test_table")
    s = ""
    for row in cur.fetchAll():
        s = s + row[0] + ", " + row[1] + "<br/>"
    return s
print hello()

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')