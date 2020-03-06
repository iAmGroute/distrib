
import importlib

import GetLatestBlockID

modules = [
    GetLatestBlockID
]
handlers = {m.CMD: m for m in modules}

class NeighborRPC:

    def __init__(self, neighbor):
        self.neighbor = neighbor
        self.nbc      = neighbor.node.nbc

    def request(self, cmd):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.request(self)

    def respond(self, cmd, data):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.request(self, data)

    def process(self, cmd, data):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.request(self, data)

    def getLatestBlockID(self):
        return GetLatestBlockID.request(self)

