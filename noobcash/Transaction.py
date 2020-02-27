
class Transaction:

    def __init__(self):
        self.signature     = None
        self.thisHash      = None
        self.senderAddress = None
        self.inputs        = None
        self.outputs       = None

    @staticmethod
    def fromJson(data):
        tx = Transaction()
        tx.signature     = bytes.fromhex(data[0])
        tx.thisHash      = bytes.fromhex(data[1])
        tx.senderAddress = bytes.fromhex(data[2])
        tx.inputs        = [
            bytes.fromhex(inputTxHash)
            for inputTxHash in data[3]
        ]
        tx.outputs       = []
        for [outputAddress, amount] in data[4]:
            tx.outputs.append((bytes.fromhex(outputAddress), amount))
        return tx

    def toJson(self):
        data = [
            self.signature.hex(),
            self.thisHash.hex(),
            self.senderAddress.hex(),
            [
                inputTxHash.hex()
                for inputTxHash in self.inputs
            ],
            [
                [outputAddress.hex(), amount]
                for (outputAddress, amount) in self.outputs
            ]
        ]
        return data

