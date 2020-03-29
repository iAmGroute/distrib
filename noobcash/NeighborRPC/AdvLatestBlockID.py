# Advertise our latest block ID to our neighbor.
# `self` is instance of `NeighborRPC`

CMD = b'ALBID...'

def request(self):
    with self.nbc as nbc:
        lastBlockID = nbc.blockchain.getLastBlockID()
    data        = lastBlockID.to_bytes(8, 'little')
    return self.neighbor.sendRequest(CMD, data, noReply=True)

def respond(self, data):
    assert len(data) == 8
    lastBlockID = int.from_bytes(data[0:8], 'little')
    self.setLastBlockID(lastBlockID)
    # Possible improvement: call request(self) if behind
    return None

def process(self, data):
    # pylint: disable=unused-argument
    assert False

