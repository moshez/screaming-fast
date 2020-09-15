import os
import klein
import treq
from twisted.internet import reactor
from twisted.web import client as twclient
from twisted.internet import defer

CLIENT = treq.client.HTTPClient(twclient.Agent(reactor))
MEAN = os.environ['MEAN']
FANOUT = int(os.environ["FANOUT"])
URL = f'http://localhost:8080/slow?mean={MEAN}'

from klein import app

@app.route('/')
async def hello_world(request):
    all_values = await defer.gatherResults([
        CLIENT.get(URL).addCallback(treq.json_content)
        for x in range(FANOUT)
    ])
    total = sum(res["value"] for res in all_values)
    return f'Total {total}'

app.run(host="127.0.0.1", port=8081)
