# Get the latest block headers of our neighbor.
# `self` is instance of `NeighborRPC`

import Constants

from Block import Block

CMD = b'GBHS....'

def request(self, fromID, toID):
    data  = fromID.to_bytes(8, 'little')
    data +=   toID.to_bytes(8, 'little')
    return self.neighbor.sendRequest(CMD, data)

def respond(self, data):
    assert len(data) == 16
    fromID = int.from_bytes(data[ 0: 8], 'little')
    toID   = int.from_bytes(data[ 8:16], 'little')
    blocks = self.nbc.blockchain.getBlocks(fromID, toID)
    reply = b''.join([
        b.getHeaderBytes()
        for b in blocks
    ])
    return reply

def process(self, data):
    # pylint: disable=unused-argument
    headerSize = Constants.BLOCK_HEADER_SIZE
    blocks = []
    for i in range(0, len(data), headerSize):
        b = Block()
        b.setHeaderBytes(data[i : i + headerSize])
        blocks.append(b)
    return blocks

