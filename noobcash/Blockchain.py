
import json

from Block import Block

class Blockchain:

    def __init__(self, filename):
        self.filename = filename
        self.blocks   = []
        self.utxos    = {} # address -> list of (tx, amount)
        self.loaded   = self.load()
        # TODO: remove
        if len(self.blocks) == 0:
            self.blocks.append(Block.fromJson([0, '00000000', '10101010', '01000000', '01234567', []]))

    def load(self):
        try:
            with open(self.filename) as f:
                while True:
                    line = f.readline()
                    if not line:
                        break
                    if not line.startswith('> '):
                        continue
                    try:
                        data = json.loads(line[2:])
                    except json.JSONDecodeError:
                        break
                    self.blocks.append(Block.fromJson(data['b']))
            return True
        except FileNotFoundError:
            return False

    def save(self):
        with open(self.filename, 'w') as f:
            f.write('# Blockchain dump\n')
            for block in self.blocks:
                data = {
                    'b': Block.toJson(block)
                }
                f.write('\n> ' + (json.dumps(data)))
            f.write('\n')

    def addBlock(self, block):
        last = self.blocks[-1]
        if block.myID == last.myID + 1 and block.prevHash == last.thisHash:
            self.blocks.append(block)
            self.save()
            return True
        else:
            return False

    def getBlock(self, blockID):
        return self.blocks[blockID] if blockID < len(self.blocks) else None

    def getLastBlockID(self):
        return len(self.blocks) - 1

    def getUTXOs(self, address):
        utxos = self.utxos.get(address, [])
        return utxos.copy()

    def getBalance(self, address):
        utxos = self.getUTXOs(address)
        return sum([amount for tx, amount in utxos])

    def getBlocks(self, fromID, toID):
        # Returns a (new) list of the current blockchain's blocks
        return self.blocks[fromID:toID]

    def validateHeaders(self, blockHeaders):
        try:
            common   = 0
            i        = blockHeaders[0].myID
            prevHash = blockHeaders[0].prevHash
            for bh in blockHeaders:
                assert i == bh.myID
                if i < len(self.blocks) and self.blocks[i].thisHash == bh.thisHash:
                    common = i + 1
                else:
                    assert bh.prevHash == prevHash
                    # TODO: assert hash(bh.nonce + bh.thisHash + bh.prevHash).startswith(b'\x00' * difficulty)
                prevHash = bh.thisHash
                i += 1
            return True, common
        except (IndexError, AssertionError):
            return False, 0

    def trySwapAt(self, height, blocks):
        if height + len(blocks) > len(self.blocks):
            self.blocks = self.blocks[:height] + blocks
            self.save()
            return True
        else:
            return False

