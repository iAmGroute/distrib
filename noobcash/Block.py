
from hashlib import sha256

from Common.Generic import listToBytes

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

    def calcPowHash(self):
        return sha256().update(self.nonce + self.thisHash + self.prevHash).digest()

    def isHeaderValid(self, dif):
        powHash = self.calcPowHash()
        return int.from_bytes(powHash[:8], 'big') < dif

    def calcThisHash(self):
        h = sha256()
        h.update(self.prevHash + self.timestamp)
        h.update(listToBytes(self.txs, lambda tx: tx.toBytes()))
        return h.digest()

    def isBodyValid(self):
        return self.thisHash == self.calcThisHash() and all([tx.isValid() for tx in self.txs])

    def isValid(self, dif):
        return self.isHeaderValid(dif) and self.isBodyValid()

