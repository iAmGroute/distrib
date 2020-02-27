
from Transaction import Transaction

class Block:

    def __init__(self):
        self.nonce     = None
        self.thisHash  = None
        self.prevHash  = None
        self.timestamp = None
        self.txs       = None

    @staticmethod
    def fromJson(data):
        b = Block()
        b.nonce     = bytes.fromhex(data[0])
        b.thisHash  = bytes.fromhex(data[1])
        b.prevHash  = bytes.fromhex(data[2])
        b.timestamp = bytes.fromhex(data[3])
        b.txs       = [
            Transaction.fromJson(tx)
            for tx in data[4]
        ]
        return b

    def toJson(self):
        data = [
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

