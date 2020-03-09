
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

