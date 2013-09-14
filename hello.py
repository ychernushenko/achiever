import os
import urlparse
from flask import Flask, render_template, send_from_directory
from goals import goal

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    return goal()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
