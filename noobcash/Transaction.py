
from Common.Generic import listToBytes

import NbcCrypto

from TransactionRef    import TransactionRef
from TransactionOutput import TransactionOutput

class Transaction:

    def __init__(self):
        # Signature
        self.signature     = b''
        # Content
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

    def getContentBytes(self):
        res = self.senderAddress                                   \
            + listToBytes(self.inputs,  lambda txi: txi.toBytes()) \
            + listToBytes(self.outputs, lambda txo: txo.toBytes())
        return res

    def toBytes(self):
        return self.signature + self.getContentBytes()

    def isSignatureValid(self):
        return self.signature and self.senderAddress \
            and NbcCrypto.verifyByAddress(
                address   = self.senderAddress,
                signature = self.signature,
                data      = self.getContentBytes()
            )

    def areInputsUnique(self):
        ins = [(txi.blockID, txi.indexInBlock) for txi in self.inputs]
        return len(ins) == len(set(ins))

    def areOutputsUnique(self):
        outs = [txo.address for txo in self.outputs]
        return len(outs) == len(set(outs))

    def isValid(self):
        return self.isSignatureValid() and self.areInputsUnique() and self.areOutputsUnique()

