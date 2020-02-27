
class Miner:

    def __init__(self, myNode):
        self.myNode     = myNode
        self.keepMining = False

    def runForever(self):
        print('Mining started')
        self.keepMining = True
        while self.keepMining:
            self.mineOneBlock()

    def mineOneBlock(self):
        # pylint: disable=no-self-use
        j = 0
        for i in range(10 ** 8):
            j += i if i % 7 else -5 * i
        print('Mined block', j)

