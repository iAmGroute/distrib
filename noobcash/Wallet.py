
import NbcCrypto

class Wallet:

    def __init__(self, nbc, keyFile):
        self.nbc     = nbc
        self.keyFile = keyFile
        self.key     = None
        self.address = None
        if not self.loadKey():
            self.generateKey()

    def _setKey(self, key):
        self.key     = key
        self.address = NbcCrypto.getAddress(key)

    def loadKey(self):
        try:
            with open(self.keyFile, 'rb') as f:
                key = NbcCrypto.keyFromPEM(f.read())
                self._setKey(key)
            return True
        except (FileNotFoundError, ValueError):
            return False

    def generateKey(self):
        key = NbcCrypto.generateKey()
        self._setKey(key)
        with open(self.keyFile, 'wb') as f:
            f.write(NbcCrypto.keyToPEM(key))

    def signTransaction(self, tx):
        tx.senderAddress = self.address
        content          = tx.getContentBytes()
        tx.signature     = NbcCrypto.sign(self.key, content)

    def getBalance(self):
        return self.nbc.blockchain.getBalance(self.address)

    def getUTXOs(self):
        return self.nbc.blockchain.getUTXOs(self.address)
