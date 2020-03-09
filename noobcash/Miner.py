
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
        b.myID      = len(self.nbc.blockchain.blocks)
        b.prevHash  = self.nbc.blockchain.blocks[b.myID - 1].thisHash
        b.timestamp = (int(time.time()) & 0xFFFFFFFF).to_bytes(4, 'little')
        b.txs       = []
        b.nonce     = b'....'
        j = 0
        for i in range(random.randrange(1, 11) * (10 ** 7)):
            j += i if i % 7 else -5 * i
        b.thisHash  = (j & 0xFFFFFFFF).to_bytes(4, 'little')
        ok = self.nbc.blockchain.addBlock(b)
        print('Mined block', b.myID, 'valid' if ok else 'stale')

