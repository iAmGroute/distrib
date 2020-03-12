
class TransactionOutput:

    def __init__(self, outputAddress, amount, spentAtBlock=0):
        # Content
        self.outputAddress = outputAddress
        self.amount        = amount
        # Cache
        self.spentAtBlock  = spentAtBlock

    @staticmethod
    def fromJson(data):
        return TransactionOutput(bytes.fromhex(data[0]), data[1])

    def toJson(self):
        return [self.outputAddress.hex(), self.amount.hex()]

