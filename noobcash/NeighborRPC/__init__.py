
from . import AdvLatestBlockID
from . import AdvPublicKey
from . import AdvTransaction
from . import GetBlock
from . import GetBlockHeaders

modules = [
    AdvLatestBlockID,
    AdvPublicKey,
    AdvTransaction,
    GetBlock,
    GetBlockHeaders,
]
handlers = {m.CMD: m for m in modules}

class NeighborRPC:

    def __init__(self, neighbor):
        self.neighbor    = neighbor
        self.nbc         = neighbor.node.app
        self.lastBlockID = 0
        self.isSyncing   = False
        self.advPublicKey()

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

    def advPublicKey(self):
        return AdvPublicKey.request(self)

    def advTransaction(self, tx):
        return AdvTransaction.request(self, tx)

    def getBlock(self, blockID, blockHash):
        return GetBlock.request(self, blockID, blockHash)

    def getBlockHeaders(self, fromID, toID):
        return GetBlockHeaders.request(self, fromID, toID)

    def setLastBlockID(self, lastBlockID):
        self.lastBlockID = lastBlockID
        with self.nbc as nbc:
            nbc.foundBlockID(self, lastBlockID)

