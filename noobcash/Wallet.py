
class Wallet:

    def __init__(self, nbc, keyFile):
        self.nbc    = nbc
        self.keyFile = keyFile
        self.pubkey  = None
        self.privkey = None
        if not self.loadKeys():
            self.generateKeys()

    def loadKeys(self):
        try:
            with open(self.keyFile) as f:
                # TODO: read pem data
                f.read()
                self.pubkey  = b'ABCDEF'
                self.privkey = b'QWERTY'
            return True
        except FileNotFoundError:
            return False

    def generateKeys(self):
        # TODO: generate random RSA keys
        self.pubkey  = b'ABCDEF'
        self.privkey = b'QWERTY'
        with open(self.keyFile, 'w') as f:
            # TODO: write pem data
            f.write('PEM keys go here\n')

    def getBalance(self):
        return self.nbc.blockchain.getBalance(self.pubkey)

    def getUTXOs(self):
        return self.nbc.blockchain.getUTXOs(self.pubkey)
