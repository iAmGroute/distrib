
import json

from Block import Block

class Blockchain:

    def __init__(self, filename):
        self.filename = filename
        self.blocks   = []
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
                    data = json.loads(line[2:])
                    self.addBlock(Block.fromJson(data['b']))
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
        # TODO: validate
        self.blocks.append(block)
        self.save()
        return True

