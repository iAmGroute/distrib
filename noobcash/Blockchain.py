
import json

from Block import Block

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
            self.blocks.append(Block.fromJson(data['b']))
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
        return sum([amount for tx, amount in utxos])

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

    def _txfromref(self, txref):
        bId, index = txref.blockID, txref.indexInBlock
        tx = self.blocks[bId].txs[index]
        return tx

    def _validate_transaction(self, tx, utxos):
        # signature and etc check
        if not tx.isValid():
            return False

        senderUtxos = utxos[tx.senderAddress]
        sendertxs = []
        for txref, amount in senderUtxos:
            sendertxs.append((self._txfromref(txref), amount))
        # inputs iteration
        valid_trans = False
        total_in = 0
        for txi in tx.inputs:
            # check if txi matches one of senderUtxos
            txi = self._txfromref(txi)
            for stx in sendertxs:
                if txi.senderAddress == stx[0].senderAddress:
                    total_in = stx[1]
                    valid_trans = True
                    break
            if valid_trans:
                break
            # also keep track of total NBCs
            #bId, index = txi.blockID, txi.indexInBlock
            # ...
        if not valid_trans:
            return False

        # outputs iteration
        valid_trans = False
        total_out = 0
        for txi in tx.outputs:
            total_out += txi.amount
            # check that the outputs sum up to the same NBCs
            if total_in == total_out:
                valid_trans = True
        if not valid_trans:
            return False
        else:
            return True

    # TODO: complete
    def _rollbackUtxos(self, height):
        utxos = self.utxos.copy()
        # undo the effect of blocks[height:] to the utxos
        for block in blocks[-1: height: -1]:
            for index,tx in enumerate(block.txs):
                # no checks need to be done here
                senderUtxos = utxos[tx.senderAddress]
                #  from the utxos and add the inputs

                # remove the outputs from utxos
                for txi in tx.outputs:
                    del utxos[txi.address]

                # add the inputs to utxos
                for txi in tx.inputs:
                    txi = self._txfromref(txi)
                    address = txi.senderAddress
                    tref = TransactionRef(block.myID, index)
                    utxos.update(address=[(tref, txi.amount)])

        return utxos

    # TODO: complete
    def _addBlocks(self, blocks):
        # `blocks` need to already be valid,
        # only transaction inputs and outputs will be checked
        if not blocks:
            return False
            
        height = blocks[0].myID  #why height is equal to blocks[0] and not blocks[-1]????
        utxos = self._rollbackUtxos(height)
        try:
            for block in blocks:
                for index, tx in enumerate(block.txs):

                    # validate transaction
                    valid = self._validate_transaction(tx, utxos)
                    if not valid:
                        return False

                    # then remove the inputs from the utxos and add the outputs

                    # remove inputs from utxos
                    for txi in tx.inputs:
                        txi = self._txfromref(txi)
                        del utxos[txi.senderAddress]

                    # add outputs in utxos
                    for txi in tx.outputs:
                        # add to utxo: key->receiver_ref  value->(sender_tref, amount)
                        receiver_add = txi.address
                        sender_tref = TransactionRef(block.myID, index)
                        utxos.update(receiver_add=[(sender_tref, txi.amount)])


        except (KeyError, IndexError, AssertionError):
            return False
        self.blocks = self.blocks[:height] + blocks
        self.utxos = utxos
        self.save(height)
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
