# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # A "good" way to use a secret, loaded from an environment variable
    # We will use this to show the "bad" way later
    api_key = os.environ.get('API_KEY', 'default_key_value')
    return f'Hello, GitSecOps! My key starts with: {api_key[:4]}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)