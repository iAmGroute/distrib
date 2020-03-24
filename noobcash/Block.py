
from Transaction import Transaction

class Block:

    def __init__(self):
        # Header
        self.myID      = None
        self.nonce     = None
        self.thisHash  = None
        self.prevHash  = None
        # Body
        self.timestamp = None
        self.txs       = None

    def __repr__(self):
        return f'Block({self.myID}, {self.nonce.hex()}, {self.thisHash.hex()}, {self.prevHash.hex()})'

    @staticmethod
    def fromJson(data):
        b = Block()
        b.myID      = data[0]
        b.nonce     = bytes.fromhex(data[1])
        b.thisHash  = bytes.fromhex(data[2])
        b.prevHash  = bytes.fromhex(data[3])
        b.timestamp = bytes.fromhex(data[4])
        b.txs       = [
            Transaction.fromJson(tx)
            for tx in data[5]
        ]
        return b

    def toJson(self):
        data = [
            self.myID,
            self.nonce.hex(),
            self.thisHash.hex(),
            self.prevHash.hex(),
            self.timestamp.hex(),
            [
                tx.toJson()
                for tx in self.txs
            ]
        ]
        return data

    def getHeaderBytes(self):
        res  = self.myID.to_bytes(8, 'little')
        res += self.nonce
        res += self.thisHash
        res += self.prevHash
        return res

    def setHeaderBytes(self, data):
        self.myID     = int.from_bytes(data[ 0: 8], 'little')
        self.nonce    = data[ 8:16]
        self.thisHash = data[16:48]
        self.prevHash = data[48:80]

    def isValid(self):
        # TODO:
        # hash(prevHash + timestamp + txs) == thisHash
        # and
        # hash(nonce + thisHash + prevHash).startsWith(b'0' * difficulty)
        return self.myID >= 0

