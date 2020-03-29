
import time
import asyncio

from Block      import Block
from Blockchain import Blockchain
from Wallet     import Wallet

class NBC:

    def __init__(self, blockchainFile, keyFile, node, miner):
        self.blockchain = Blockchain(blockchainFile)
        self.wallet     = Wallet(self, keyFile)
        self.node       = node
        self.node.setApp(self)
        self.miner      = miner
        self.miner.setNBC(self)
        self.difficulty = 1 << (64 - 25)
        self.loop       = None

    async def main(self):
        while True:
            await asyncio.sleep(4)
            self.node.gossip(lambda rpc: rpc.advLatestBlockID())

    def runAsync(self, coroutine):
        self.loop.create_task(coroutine)

    def runForever(self):
        self.loop = asyncio.new_event_loop()
        self.runAsync(self.node.runServer())
        self.runAsync(self.main())
        self.loop.run_forever()

    # A block is found externally (by NeighborRPC)
    def foundBlockID(self, neighborRPC, lastBlockID):
        if neighborRPC.isSyncing:
            return
        if lastBlockID > self.blockchain.getLastBlockID():
            self.runAsync(self.consensusWith(neighborRPC, lastBlockID))

    # Miner calls this to get a block to mine
    def getBlockToMine(self):
        b = Block()
        b.myID      = len(self.blockchain.blocks)
        b.prevHash  = self.blockchain.blocks[b.myID - 1].thisHash
        b.timestamp = int(time.time()).to_bytes(8, 'little')
        b.txs       = []
        b.thisHash  = b.calcThisHash()
        return b, self.difficulty

    # Miner calls this when a block is mined
    def blockMined(self, block):
        ok = self.blockchain.addMinedBlock(block)
        print('Mined block', block.myID, 'valid' if ok else 'stale')
        if ok:
            self.node.multicast(lambda rpc: rpc.advLatestBlockID())

    async def consensusWith(self, neighborRPC, lastBlockID):
        neighborRPC.isSyncing = True
        await self._consensusWith(neighborRPC, lastBlockID)
        neighborRPC.isSyncing = False

    async def _consensusWith(self, neighborRPC, lastBlockID):
        print('Consensus with', neighborRPC.neighbor.peerName, 'started')
        fromID = max(self.blockchain.getLastBlockID() - 10, 0)
        toID   = lastBlockID + 1
        blocks = []
        while True:
            print('Consensus: asking block headers from', fromID, 'to', toID)
            newblocks = await neighborRPC.getBlockHeaders(fromID, toID)
            if not newblocks:
                return
            print('Consensus: got block headers')
            ok, common = self.blockchain.validateHeaders(newblocks, self.difficulty)
            print(ok, common, 'common', lastBlockID - common, 'different')
            blocks = newblocks + blocks
            if not ok:
                return
            if common > 0:
                blocks = blocks[common - blocks[0].myID:]
                await self._doConsensusWith(neighborRPC, blocks, common)
                break
            # Ask for more (older) blocks
            if fromID > 0:
                toID   = fromID
                fromID = max(fromID - 100, 0)
            else:
                # We have every block, but still can't find a common start,
                # so we will assume bad neighbor/connection.
                print('Consensus: BAD neighbor')
                neighborRPC.neighbor.disconnect()

    async def _doConsensusWith(self, neighborRPC, blocks, common):
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
        if swapped:
            self.miner.keepMining = False

