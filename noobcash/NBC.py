
from Blockchain import Blockchain
from Wallet     import Wallet

class NBC:

    def __init__(self, blockchainFile, keyFile):
        self.blockchain = Blockchain(blockchainFile)
        self.wallet     = Wallet(self, keyFile)

