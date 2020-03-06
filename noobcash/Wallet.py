
class Wallet:

    def __init__(self, node, pubkey):
        self.node   = node
        self.pubkey = pubkey

    def getBalance(self):
        return self.node.blockchain.getBalance(self.pubkey)

    def getUTXOs(self):
        return self.node.blockchain.getUTXOs(self.pubkey)


