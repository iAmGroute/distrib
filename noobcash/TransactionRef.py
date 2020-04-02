
class TransactionRef:

    def __init__(self, blockID, indexInBlock):
        self.blockID      = blockID
        self.indexInBlock = indexInBlock

    def __repr__(self):
        return f'@{self.blockID}:{self.indexInBlock}'

    def __eq__(self, other):
        return  self.blockID      == other.blockID \
            and self.indexInBlock == other.indexInBlock

    def __hash__(self):
        return hash((self.blockID, self.indexInBlock))

    @staticmethod
    def fromJson(data):
        return TransactionRef(data[0], data[1])

    def toJson(self):
        return [self.blockID, self.indexInBlock]

    def toBytes(self):
        res = self.blockID.to_bytes(8, 'little') \
            + self.indexInBlock.to_bytes(8, 'little')
        return res

