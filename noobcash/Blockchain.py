
import json

from Common.Generic import find
from Block          import Block
from TransactionRef import TransactionRef

class Blockchain:

    def __init__(self, filename):
        self.blocks = []
        self.utxos = {}  # address -> list of (tx_ref, amount)
        self.file = None
        self.filePositions = []
        self.load(filename)

    def __del__(self):
        if self.file is not None:
            self.file.close()

    def load(self, filename):
        f = open(filename, 'r+')
        self.blocks = []
        while True:
            pos = f.tell()
            line = f.readline()
            if not line:
                break
            if not line.startswith('> '):
                continue
            try:
                data = json.loads(line[2:])
            except json.JSONDecodeError:
                break
            if not self._addBlocks([Block.fromJson(data['b'])], noSave=True):
                break
            self.filePositions.append(pos)
        f.seek(pos)
        f.truncate()
        self.file = f

    def save(self, fromHeight):
        f = self.file
        # Check if we need to seek back and overwrite some blocks
        if fromHeight < len(self.filePositions):
            pos = self.filePositions[fromHeight]
            self.filePositions = self.filePositions[:fromHeight]
            f.seek(pos)
            f.truncate()
        # Write all the new blocks
        for block in self.blocks[fromHeight:]:
            self.filePositions.append(f.tell())
            data = {'b': Block.toJson(block)}
            f.write('> ' + json.dumps(data) + '\n')
        f.flush()

    def getBlock(self, blockID):
        return self.blocks[blockID] if blockID < len(self.blocks) else None

    def getLastBlockID(self):
        return len(self.blocks) - 1

    def getUTXOs(self, address):
        utxos = self.utxos.get(address, [])
        return utxos.copy()

    def getBalance(self, address):
        utxos = self.getUTXOs(address)
        return sum([amount for _, amount in utxos])

    def getBlocks(self, fromID, toID):
        # Returns a (new) list of the current blockchain's blocks
        return self.blocks[fromID:toID]

    def validateHeaders(self, blockHeaders, dif):
        try:
            common = 0
            i = blockHeaders[0].myID
            prevHash = blockHeaders[0].prevHash
            for bh in blockHeaders:
                assert i == bh.myID
                if i < len(self.blocks) and self.blocks[i].thisHash == bh.thisHash:
                    # we have this block, no need to check anything
                    common = i + 1
                else:
                    assert bh.prevHash == prevHash
                    assert bh.isHeaderValid(dif)
                prevHash = bh.thisHash
                i += 1
            return True, common
        except (IndexError, AssertionError):
            return False, 0

    def _rollbackUtxos(self, height):
        utxos = self.utxos.copy()
        # undo the effect of `self.blocks[height:]` to the utxos
        for block in self.blocks[-1 : height : -1]:
            for txIndex, tx in enumerate(block.txs):
                txRef = TransactionRef(block.myID, txIndex)
                # remove the outputs from the receivers' utxos
                for txo in tx.outputs:
                    receiverUtxos = utxos[txo.address]
                    i, _ = find(receiverUtxos, lambda utxo: utxo[0] == txRef)
                    del receiverUtxos[i]
                # and add the inputs to the sender's utxos
                senderUtxos = utxos[tx.senderAddress]
                for txi in tx.inputs:
                    inputTx = self.blocks[txi.blockID].txs[txi.indexInBlock]
                    _, txo  = find(inputTx.outputs, lambda txo: txo.address == tx.senderAddress)
                    senderUtxos.append((txi, txo.amount))
        return utxos

    # TODO: complete
    def _addBlocks(self, blocks, noSave=False):
        # `blocks` need to already be valid,
        # only transaction inputs and outputs will be checked
        if not blocks:
            return False
            
        height = blocks[0].myID  #why height is equal to blocks[0] and not blocks[-1]????
        utxos = self._rollbackUtxos(height)
        try:
            for block in blocks:
                for txIndex, tx in enumerate(block.txs):
                    txRef       = TransactionRef(block.myID, txIndex)
                    senderUtxos = utxos.get(tx.senderAddress, [])
                    total       = 0
                    # remove the inputs from the sender's utxos
                    for txi in tx.inputs:
                        i, utxo = find(senderUtxos, lambda utxo: utxo[0] == txi)
                        total  += utxo[1]
                        del senderUtxos[i]
                    # and add the outputs to the receivers' utxos
                    for txo in tx.outputs:
                        total        -= txo.amount
                        receiverUtxos = utxos.get(txo.address, [])
                        if not receiverUtxos:
                            utxos[txo.address] = receiverUtxos
                        receiverUtxos.append((txRef, txo.amount))
                    # make sure the total input - output is zero,
                    # except for block 0
                    if block.myID != 0:
                        assert total == 0
        except (KeyError, IndexError, AssertionError):
            return False
        self.blocks = self.blocks[:height] + blocks
        self.utxos  = utxos
        if not noSave: self.save(height)
        return True

    def addMinedBlock(self, block):
        # `block` is assumed to be valid if it follows the last block
        last = self.blocks[-1]
        if block.myID == last.myID + 1 and block.prevHash == last.thisHash:
            return self._addBlocks([block])
        else:
            return False

    def trySwapAt(self, height, blocks):
        # `blocks` are assumed to be valid
        # and that their headers form a valid chain,
        # so we only need to check their transactions' inputs and outputs
        if height > 1 and height + len(blocks) > len(self.blocks):
            return self._addBlocks(blocks)
        else:
            return False
