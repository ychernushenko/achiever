import os
import psycopg2
import urlparse
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
    

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

@app.route('/')
def hello():
    db = psycopg2.connect(database =url.path[1],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port)
    cur = db.cursor()
    cur.execute("SELECT * FROM test_table")
    s = ""
    for row in cur.fetchAll():
        s = s + row[0] + ", " + row[1] + "<br/>"
    print s
    return s


@app.route('/other')
def other():
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
