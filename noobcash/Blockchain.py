
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
            self.addBlock(Block.fromJson(['00000000', '10101010', '01000000', '01234567', []]))

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
                    self._addBlock(Block.fromJson(data['b']))
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

    def _addBlock(self, block):
        last = self.blocks[-1]
        if block.myID == last.myID + 1 and block.prevHash == last.thisHash:
            self.blocks.append(block)
            return True
        else:
            return False

    def addBlock(self, block):
        ok = self._addBlock(block)
        if ok:
            self.save()
        return ok

    def getUTXOs(self, address):
        utxos = self.utxos.get(address, [])
        return utxos.copy()

    def getBalance(self, address):
        utxos = self.getUTXOs(address)
        return sum([amount for tx, amount in utxos])

    def getBlocks(self):
        # Returns a (new) list of the current blockchain's blocks
        return self.blocks.copy()

