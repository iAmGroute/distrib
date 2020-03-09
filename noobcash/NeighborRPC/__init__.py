
import importlib

from . import AdvLatestBlockID

modules = [
    AdvLatestBlockID,
]
handlers = {m.CMD: m for m in modules}

class NeighborRPC:

    def __init__(self, neighbor):
        self.neighbor = neighbor
        self.nbc      = neighbor.node.nbc
        self.lastBlockID = 0

    def request(self, cmd):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.request(self)

    def respond(self, cmd, data):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.respond(self, data)

    def process(self, cmd, data):
        handler = handlers.get(cmd)
        assert handler is not None
        return handler.process(self, data)

    def advLatestBlockID(self):
        return AdvLatestBlockID.request(self)

    def setLatestBlockID(self, lastBlockID):
        self.lastBlockID = lastBlockID
