import os
import psycopg2
import urlparse
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
