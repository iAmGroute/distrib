
from Blockchain import Blockchain
from Wallet     import Wallet

class NBC:

    def __init__(self, blockchainFile, keyFile):
        self.blockchain = Blockchain(blockchainFile)
        self.wallet     = Wallet(self, keyFile)
        self.node       = None

    def foundBlockID(self, neighborRPC, lastBlockID):
        if lastBlockID > self.blockchain.getLastBlockID():
            self.node.runAsync(self.consensusWith(neighborRPC))

    async def consensusWith(self, neighborRPC):
        blocks = await neighborRPC.getBlockHeaders()
        if not blocks:
            return
        ok, common = self.blockchain.validateHeaders(blocks)
        if ok:
            blocks = blocks[common:]
            for block in blocks:
                b = await neighborRPC.getBlock(block.myID, block.thisHash)
                if not b:
                    return
                block.timestamp = b.timestamp
                block.txs       = b.txs
                if not block.isValid():
                    return
            self.blockchain.trySwapAt(common, blocks)

