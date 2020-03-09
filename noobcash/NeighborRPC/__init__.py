
import importlib

from . import AdvLatestBlockID
from . import GetBlockHeaders

modules = [
    AdvLatestBlockID,
    GetBlockHeaders,
]
handlers = {m.CMD: m for m in modules}

class NeighborRPC:

    def __init__(self, neighbor):
        self.neighbor    = neighbor
        self.nbc         = neighbor.node.nbc
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

    def getBlockHeaders(self):
        return GetBlockHeaders.request(self)

    def setLastBlockID(self, lastBlockID):
        self.lastBlockID = lastBlockID
        self.nbc.foundBlockID(self, lastBlockID)

