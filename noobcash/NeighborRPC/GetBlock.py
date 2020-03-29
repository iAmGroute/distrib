# Get the contents of our neighbor's block with a given ID and hash.
# `self` is instance of `NeighborRPC`

import json

from Block import Block

CMD = b'GB......'

def request(self, blockID, blockHash):
    data  = blockID.to_bytes(8, 'little')
    data += blockHash
    return self.neighbor.sendRequest(CMD, data)

def respond(self, data):
    assert len(data) == 40
    blockID   = int.from_bytes(data[ 0: 8], 'little')
    blockHash = data[ 8:40]
    with self.nbc as nbc:
        block = nbc.blockchain.getBlock(blockID)
    if block and block.thisHash == blockHash:
        reply = json.dumps(block.toJson()).encode('utf-8')
    else:
        reply = b''
    return reply

def process(self, data):
    # pylint: disable=unused-argument
    if data:
        try:
            block = Block.fromJson(json.loads(data.decode('utf-8')))
            return block
        except json.JSONDecodeError:
            return None
    return None

