import os
import urlparse
from flask import Flask, render_template, send_from_directory
from goals import goal
from login import login

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def main():
    return login()

@app.route('/<path:filename>.html', methods=['POST', 'GET'])
def channel(filename):
    return send_from_directory('templates', filename+".html")

@app.route('/<userid>', methods=['POST', 'GET'])
def hello(userid):
    return goal(userid)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
