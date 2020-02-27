# Get the latest block ID of our neighbor.
# `self` is instance of `Neighbor`

CMD = b'GLBID...'

def request(self):
    return self.sendRequest(CMD, b'')

def respond(self, data):
    assert len(data) == 0
    lastBlockID = len(self.node.blockchain.blocks) - 1
    reply = lastBlockID.to_bytes(8, 'little')
    return reply

def process(self, data):
    assert len(data) == 8
    lastBlockID      = int.from_bytes(data[0:8], 'little')
    self.lastBlockID = lastBlockID
    return lastBlockID

