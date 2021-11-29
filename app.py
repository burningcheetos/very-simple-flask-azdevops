import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    env = os.environ.get('ENVIRONMENT')
    if env:
        return env
    return 'Hello, World'

# export FLASK_ENV=app.py
app.run(host='0.0.0.0', port=8000)
