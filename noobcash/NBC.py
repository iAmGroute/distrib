
import time
import asyncio

from collections        import deque

import Constants

from Block              import Block
from Blockchain         import Blockchain
from Wallet             import Wallet
from Transaction        import Transaction
from TransactionOutput  import TransactionOutput

class NBC:

    def __init__(self, blockchainFile, keyFile, node, miner):
        self.blockchain = Blockchain(blockchainFile)
        self.wallet     = Wallet(self, keyFile)
        self.node       = node
        self.miner      = miner
        self.difficulty = 1 << (64 - Constants.DIFFICULTY)
        self.loop       = None
        self.mempool    = deque()

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

    def createTransaction(self, address, amount):
        if amount < 0:
            return None
        tx               = Transaction()
        tx.senderAddress = self.wallet.address
        # find inputs from utxos and calculate total input value
        inputTotal = 0
        utxos      = self.blockchain.utxos.get(tx.senderAddress, [])
        for txRef, txAmount in utxos:
            tx.inputs.append(txRef)
            inputTotal += txAmount
        if inputTotal < amount:
            return None
        # 2 outputs
        # one output for receiver
        tx.outputs.append(TransactionOutput(address, amount))
        # and another for the change, back to sender
        tx.outputs.append(TransactionOutput(tx.senderAddress, inputTotal - amount))
        # Put a chicken stamp in the transaction so Alice can eat it :)
        self.wallet.signTransaction(tx)
        return tx

    # Miner calls this to get a block to mine
    def getBlockToMine(self):
        b = Block()
        b.myID      = len(self.blockchain.blocks)
        b.prevHash  = self.blockchain.blocks[b.myID - 1].thisHash
        b.timestamp = int(time.time()).to_bytes(8, 'little')
        b.txs       = []
        for _ in range(Constants.CAPACITY):
            if self.mempool:
                tx = self.mempool.pop()
                b.txs.append(tx)
            else:
                break
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
            if ok:
                print(common, 'common', lastBlockID - common, 'different')
            else:
                print('Consensus: BAD neighbor - invalid headers')
                neighborRPC.neighbor.disconnect()
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
                print('Consensus: BAD neighbor - no common start')
                neighborRPC.neighbor.disconnect()

    async def _doConsensusWith(self, neighborRPC, blocks, common):
        for block in blocks:
            b = await neighborRPC.getBlock(block.myID, block.thisHash)
            if not b:
                return
            block.timestamp = b.timestamp
            block.txs       = b.txs
            if not block.isValid(self.difficulty):
                print('Consensus: INVALID block', block.myID)
                return
        print('Consensus: trying to swap')
        swapped = self.blockchain.trySwapAt(common, blocks)
        print(swapped)
        if swapped:
            self.miner.keepMining = False

