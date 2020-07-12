import os
import flask
import httpx

CLIENT = httpx.Client()
URL = 'http://localhost:8080/slow?' + '&'.join(f"slow={float(part)}" for part in os.environ.get("SLOW", "").split(",") if part)
FANOUT = int(os.environ.get("FANOUT", "1"))

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    all_values = sum(CLIENT.get(URL).json()["value"] for x in range(FANOUT))
    return f'Total {all_values}'
