
import time
import random
import asyncio

from Block      import Block
from Blockchain import Blockchain
from Wallet     import Wallet

class NBC:

    def __init__(self, blockchainFile, keyFile, node):
        self.blockchain = Blockchain(blockchainFile)
        self.wallet     = Wallet(self, keyFile)
        self.node       = node
        self.node.setApp(self)

    async def main(self):
        while True:
            await asyncio.sleep(4)
            self.node.gossip(lambda rpc: rpc.advLatestBlockID())

    # A block is found externally (by NeighborRPC)
    def foundBlockID(self, neighborRPC, lastBlockID):
        if neighborRPC.isSyncing:
            return
        if lastBlockID > self.blockchain.getLastBlockID():
            self.node.runAsync(self.consensusWith(neighborRPC))

    # Miner calls this to get a block to mine
    def getBlockToMine(self):
        b = Block()
        b.myID      = len(self.blockchain.blocks)
        b.thisHash  = random.randrange(1000).to_bytes(4, 'little')
        b.prevHash  = self.blockchain.blocks[b.myID - 1].thisHash
        b.timestamp = (int(time.time()) & 0xFFFFFFFF).to_bytes(4, 'little')
        b.txs       = []
        return b

    # Miner calls this when a block is mined
    def blockMined(self, block):
        ok = self.blockchain.addBlock(block)
        print('Mined block', block.myID, 'valid' if ok else 'stale')
        if ok:
            self.node.multicast(lambda rpc: rpc.advLatestBlockID())

    async def _consensusWith(self, neighborRPC):
        print('Consensus with', neighborRPC.neighbor.peerName, 'started')
        blocks = await neighborRPC.getBlockHeaders()
        if not blocks:
            return
        print('Consensus: got block headers')
        ok, common = self.blockchain.validateHeaders(blocks)
        print(ok, common, 'common', len(blocks) - common, 'different')
        if ok:
            blocks = blocks[common:]
            for block in blocks:
                b = await neighborRPC.getBlock(block.myID, block.thisHash)
                if not b:
                    return
                block.timestamp = b.timestamp
                block.txs       = b.txs
                if not block.isValid():
                    print('Consensus: INVALID block', block.myID)
                    return
            print('Consensus: trying to swap')
            swapped = self.blockchain.trySwapAt(common, blocks)
            print(swapped)

    async def consensusWith(self, neighborRPC):
        neighborRPC.isSyncing = True
        await self._consensusWith(neighborRPC)
        neighborRPC.isSyncing = False

