
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
            self.node.runAsync(self.consensusWith(neighborRPC, lastBlockID))

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

    async def _consensusWith(self, neighborRPC, lastBlockID):
        print('Consensus with', neighborRPC.neighbor.peerName, 'started')
        fromID = max(self.blockchain.getLastBlockID() - 10, 1)
        toID   = lastBlockID + 1
        blocks = []
        while fromID > 0:
            print('Consensus: asking block headers from', fromID, 'to', toID)
            newblocks = await neighborRPC.getBlockHeaders(fromID, toID)
            if not newblocks:
                return
            print('Consensus: got block headers')
            ok, common = self.blockchain.validateHeaders(newblocks)
            print(ok, common, 'common', lastBlockID - common, 'different')
            blocks = newblocks + blocks
            if not ok:
                return
            if common > 0:
                blocks = blocks[common - blocks[0].myID:]
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
                break
            # Ask for more (older) blocks
            toID    = fromID
            fromID -= 100

    async def consensusWith(self, neighborRPC, lastBlockID):
        neighborRPC.isSyncing = True
        await self._consensusWith(neighborRPC, lastBlockID)
        neighborRPC.isSyncing = False

