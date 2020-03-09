
import importlib

from . import AdvLatestBlockID
from . import GetBlock
from . import GetBlockHeaders

modules = [
    AdvLatestBlockID,
    GetBlock,
    GetBlockHeaders,
]
handlers = {m.CMD: m for m in modules}

class NeighborRPC:

    def __init__(self, neighbor):
        self.neighbor    = neighbor
        self.nbc         = neighbor.node.app
        self.lastBlockID = 0

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

    def getBlock(self, blockID, blockHash):
        return GetBlock.request(self, blockID, blockHash)

    def setLastBlockID(self, lastBlockID):
        self.lastBlockID = lastBlockID
        self.nbc.foundBlockID(self, lastBlockID)

