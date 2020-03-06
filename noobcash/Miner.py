
import time
import random

from Block import Block

class Miner:

    def __init__(self, nbc):
        self.nbc        = nbc
        self.keepMining = False

    def runForever(self):
        print('Mining started')
        self.keepMining = True
        while self.keepMining:
            self.mineOneBlock()

    def mineOneBlock(self):
        b = Block()
        blockId = len(self.nbc.blockchain.blocks)
        b.prevHash  = self.nbc.blockchain.blocks[blockId - 1].thisHash
        b.timestamp = (int(time.time()) & 0xFFFFFFFF).to_bytes(4, 'little')
        b.txs       = []
        j = 0
        b.nonce     = b'....'
        for i in range(random.randrange(1, 11) * (10 ** 7)):
            j += i if i % 7 else -5 * i
        b.thisHash  = (j & 0xFFFFFFFF).to_bytes(4, 'little')
        self.nbc.blockchain.addBlock(b)
        print('Mined block', blockId)


