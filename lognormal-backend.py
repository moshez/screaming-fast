import json, random
from twisted.internet import task, reactor
from klein import run, route

from scipy.stats import lognorm

@route('/slow')
def slow(request):
    mean = float(request.args[b'mean'][0])
    sigma = 1.4 # hardcode
    [speed] = lognorm.rvs(sigma, size=1)
    speed *= mean
    print(speed)
    return task.deferLater(reactor, speed, json.dumps, dict(value=speed))

run("localhost", 8080)
