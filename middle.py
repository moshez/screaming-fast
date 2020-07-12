import os
import flask
import httpx

CLIENT = httpx.Client()
URL = 'http://localhost:8080/slow?' + '&'.join(f"slow={float(part)}" for part in os.environ.get("SLOW", "").split(",") if part)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    result = CLIENT.get(URL)
    value = result.json()['value']
    return f'Got {value}'
