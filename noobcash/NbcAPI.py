
import functools

import hug

# pylint: disable=protected-access

_nbc = None

def init(nbcInstance):
    global _nbc
    _nbc = nbcInstance

def usingNBC(func):
    @functools.wraps(func)
    def newFunc(*args, **kwargs):
        global _nbc
        with _nbc as cm:
            res = func(cm, *args, **kwargs)
        return res
    return newFunc

@hug.get()
@usingNBC
def status(nbc):
    resp = {
        'host': nbc.node.host,
        'port': nbc.node.port,
        'neighbors': [
            {
                'connected':    neighbor.connected,
                'peerName':     neighbor.peerName,
                'lastBlockID':  neighbor.rpc.lastBlockID,
                'isSyncing':    neighbor.rpc.isSyncing,
                'pendingCount': len(neighbor.futures)
            }
            for neighbor in nbc.node.neighbors
        ],
        'blockchain': {
            'length': len(nbc.blockchain.blocks)
        },
        'utxos': [
            (txRef.toJson(), amount)
            for txRef, amount in nbc.wallet.getUTXOs()
        ],
        'balance': nbc.wallet.getBalance()
    }
    return resp

@hug.get()
@usingNBC
def getBlock(nbc, blockID:int, detailed:bool):
    b    = nbc.blockchain.blocks[blockID]
    resp = {
        'myID':      b.myID,
        'powHash':   b.calcPowHash().hex(),
        'nonce':     b.nonce.hex(),
        'thisHash':  b.thisHash.hex(),
        'prevHash':  b.prevHash.hex(),
        'timestamp': int.from_bytes(b.timestamp, 'little'),
        'txCount':   len(b.txs)
    }
    if detailed:
        resp['txs'] = [
            {
                'signature':     tx.signature.hex(),
                'senderAddress': tx.senderAddress.hex(),
                'inputCount' :   len(tx.inputs),
                'outputCount' :  len(tx.outputs),
                'coins':         sum([txo.amount for txo in tx.outputs])
            }
            for tx in b.txs
        ]
    return resp

@hug.get()
@usingNBC
def save(nbc):
    nbc.blockchain.save()
    return {'result': True}

@hug.get()
@usingNBC
def connectToNeighbor(nbc, host:str, port:int):
    nbc.runAsync(nbc.node.connectToNeighbor(host, port))
    return {'result': True}


@hug.get()
@usingNBC
#name t because it is defined as such in exercise requirments? :/
def t(nbc, receiver_address:str, amount:int):
    nbc.mempool.append((receiver_address, amount))
    resp = {
        'Sender_Address':       nbc.wallet.address,
        'Receiver_Address':     receiver_address,
        'Amount':               amount
    }
    return resp