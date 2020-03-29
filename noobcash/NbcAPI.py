
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
            (tx.thisHash.hex(), amount)
            for tx, amount in nbc.wallet.getUTXOs()
        ],
        'balance': nbc.wallet.getBalance()
    }
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

