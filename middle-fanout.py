import json
import os
import flask
import httpx

MEAN = os.environ['MEAN']
FANOUT = int(os.environ["FANOUT"])
CLIENT = httpx.Client(timeout=None)
URL = f'http://localhost:8080/slow?mean={MEAN}'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    all_values = sum(
        CLIENT.get(URL).json()["value"]
        for x in range(FANOUT)
    )
    return json.dumps(dict(total=all_values))
