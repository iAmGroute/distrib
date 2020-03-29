
class TransactionRef:

    def __init__(self, blockID, indexInBlock):
        self.blockID      = blockID
        self.indexInBlock = indexInBlock

    @staticmethod
    def fromJson(data):
        return TransactionRef(data[0], data[1])

    def toJson(self):
        return [self.blockID, self.indexInBlock]

    def toBytes(self):
        res = self.blockID.to_bytes(8, 'little') \
            + self.indexInBlock.to_bytes(8, 'little')
        return res

