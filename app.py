import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 8080.
    port = int(os.environ.get('PIGEON_HTTP_PORT', 8080))
    app.run(host='0.0.0.0', port=port)