
class TransactionOutput:

    def __init__(self, address, amount, spentAtBlock=0):
        # Content
        self.address = address
        self.amount  = amount
        # Cache
        self.spentAtBlock  = spentAtBlock

    def __repr__(self):
        return f'{self.amount}nbc->a.{self.address[:8].hex()}..spent@{self.spentAtBlock}'

    @staticmethod
    def fromJson(data):
        return TransactionOutput(bytes.fromhex(data[0]), data[1])

    def toJson(self):
        return [self.address.hex(), self.amount]

    def toBytes(self):
        res = self.address \
            + self.amount.to_bytes(8, 'little')
        return res

