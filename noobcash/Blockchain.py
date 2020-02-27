
import json

from Block import Block

class Blockchain:

    def __init__(self):
        self.blocks = []

    @staticmethod
    def load(filename):
        bc = Blockchain()
        with open(filename) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                if not line.startswith('> '):
                    continue
                data = json.loads(line[2:])
                bc.addBlock(Block.fromJson(data['b']))
        return bc

    def dump(self, filename):
        with open(filename, 'w') as f:
            f.write('# Blockchain dump\n')
            for block in self.blocks:
                data = {
                    'b': Block.toJson(block)
                }
                f.write('\n> ' + (json.dumps(data)))
            f.write('\n')

    def addBlock(self, block):
        self.blocks.append(block)

