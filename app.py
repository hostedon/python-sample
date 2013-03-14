import os
import json
from pyinfo import pyinfo
from flask import Flask

app = Flask(__name__)

@app.route('/')
def pyinfopage():
    return pyinfo()

@app.route('/hello')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8080.
    port = 8080

    with open("/var/run/environment.json", "r") as f:
        port = int(json.loads(f.read())['PIGEON_HTTP_PORT'])

    app.run(host='0.0.0.0', port=port)
