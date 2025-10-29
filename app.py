# app.py
# Removed hard-coded secret from source. Load secrets from environment variables instead.
from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Load API key from environment variable (do not store secrets in source)
    api_key = os.environ.get('API_KEY', 'default_key_value')
    return f'Hello, GitSecOps! My key starts with: {api_key[:4]}'


if __name__ == '__main__':
    # Allow PORT and FLASK_DEBUG to be set via environment variables for flexibility
    port = int(os.environ.get('PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', 'true').lower() in ('1', 'true', 'yes')
    app.run(debug=debug, host='0.0.0.0', port=port)