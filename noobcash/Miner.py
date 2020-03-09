
import random


def mineOneBlock(block):
    j = 0
    for i in range(random.randrange(1, 31) * (10 ** 7)):
        j += i if i % 7 else -5 * i
    block.nonce = (j & 0xFFFFFFFF).to_bytes(4, 'little')


class Miner:

    def __init__(self, nbc):
        self.nbc        = nbc
        self.keepMining = False

    def runForever(self):
        print('Mining started')
        self.keepMining = True
        while self.keepMining:
            b = self.nbc.getBlockToMine()
            mineOneBlock(b)
            self.nbc.blockMined(b)

