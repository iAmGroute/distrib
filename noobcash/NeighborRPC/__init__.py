
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
        self.neighbor     = neighbor
        self.nbc          = neighbor.node.app
        self.lastBlockID  = 0
        self.blockFutures = {} # blockID -> future
        self.isSyncing    = False

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

    def getBlockHeaders(self, fromID, toID):
        return GetBlockHeaders.request(self, fromID, toID)

    def getBlock(self, blockID, blockHash):
        isStale = lambda b: b is None or b.thisHash != blockHash
        f = self.blockFutures.get(blockID)
        if f is None or f.done() and isStale(f.result()):
            print('Asking for', blockID, blockHash)
            f = GetBlock.request(self, blockID, blockHash)
            self.blockFutures[blockID] = f
        return f

    def setLastBlockID(self, lastBlockID):
        self.lastBlockID = lastBlockID
        self.nbc.foundBlockID(self, lastBlockID)

