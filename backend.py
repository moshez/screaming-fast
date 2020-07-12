import json, random
from twisted.internet import task, reactor
from klein import run, route

@route('/slow')
def slow(request):
    speeds = list(map(float, request.args.get(b'slow', []))) or [0.01]
    return task.deferLater(reactor, random.choice(speeds), json.dumps, dict(value=5))

run("localhost", 8080)
