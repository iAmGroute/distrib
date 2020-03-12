
from TransactionRef    import TransactionRef
from TransactionOutput import TransactionOutput

class Transaction:

    def __init__(self):
        # Identity
        self.thisHash      = b'' # do we need this ?
        # Content
        self.signature     = b''
        self.senderAddress = b''
        self.inputs        = []
        self.outputs       = []

    @staticmethod
    def fromJson(data):
        tx = Transaction()
        tx.signature     = bytes.fromhex(data[0])
        tx.senderAddress = bytes.fromhex(data[1])
        tx.inputs        = [
            TransactionRef.fromJson(txi)
            for txi in data[2]
        ]
        tx.outputs       = [
            TransactionOutput.fromJson(txo)
            for txo in data[3]
        ]
        return tx

    def toJson(self):
        data = [
            self.signature.hex(),
            self.senderAddress.hex(),
            [
                txi.toJson()
                for txi in self.inputs
            ],
            [
                txo.toJson()
                for txo in self.outputs
            ]
        ]
        return data

