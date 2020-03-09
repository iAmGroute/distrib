# Get the latest block headers of our neighbor.
# `self` is instance of `NeighborRPC`

from Block import Block

CMD = b'GBHS....'

def request(self):
    return self.neighbor.sendRequest(CMD, b'')

def respond(self, data):
    assert len(data) == 0
    lastBlocks = self.nbc.blockchain.getBlocks()
    reply = b''.join([
        b.getHeaderBytes()
        for b in lastBlocks
    ])
    return reply

def process(self, data):
    # TODO: this needs to be defined as a constant somewhere
    headerSize = len(self.nbc.blockchain.blocks[0].getHeaderBytes())
    blocks = []
    for i in range(0, len(data), headerSize):
        b = Block()
        b.setHeaderBytes(data[i : i + headerSize])
        blocks.append(b)
    return blocks

