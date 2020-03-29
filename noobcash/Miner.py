
from hashlib import sha256

class Miner:

    def __init__(self):
        self.nbc        = None
        self.enabled    = False
        self.keepMining = False

    def setNBC(self, nbc):
        self.nbc = nbc

    def runForever(self):
        print('Mining enabled')
        self.enabled = True
        while self.enabled:
            with self.nbc as nbc:
                b, dif = nbc.getBlockToMine()
            print('Mining block', b.myID)
            d = b.thisHash + b.prevHash
            n = 0
            self.keepMining = True
            while self.keepMining:
                # Run 'a few' iterations without checking `keepMining`
                # more iterations -> better hashrate
                # few  iterations -> better response time
                # 100000 take around 150ms
                for _ in range(100000):
                    h = sha256()
                    n += 1
                    nonce = n.to_bytes(8, 'little')
                    h.update(nonce + d)
                    if int.from_bytes(h.digest()[:8], 'big') < dif:
                        # found it !
                        b.nonce = nonce
                        with self.nbc as nbc:
                            nbc.blockMined(b)
                        self.keepMining = False
                        break
        print('Mining disabled')

