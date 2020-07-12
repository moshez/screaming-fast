import json, random
from twisted.internet import task, reactor
from klein import run, route

@route('/slow')
def slow(request):
    speed = random.choice(list(map(float, request.args.get(b'slow', []))) or [0.01])
    return task.deferLater(reactor, speed, json.dumps, dict(value=speed))

run("localhost", 8080)
