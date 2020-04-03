
import functools

import hug

from Common.Generic import find

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
                'peerName':     neighbor.peerName,
                'guid':         neighbor.guid.hex() if neighbor.guid else None,
                'lastBlockID':  neighbor.rpc.lastBlockID,
                'connected':    neighbor.connected,
                'isSyncing':    neighbor.rpc.isSyncing,
                'pendingCount': len(neighbor.futures)
            }
            for neighbor in nbc.node.neighbors
        ],
        'blockchain': {
            'length': len(nbc.blockchain.blocks)
        },
        'wallet': {
            'address': nbc.wallet.address.hex(),
            'balance': nbc.wallet.getBalance(),
            'utxos': [
                (txRef.toJson(), amount)
                for txRef, amount in nbc.wallet.getUTXOs()
            ]
        }
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
def getTransaction(nbc, blockID:int, indexInBlock:int):
    tx   = nbc.blockchain.blocks[blockID].txs[indexInBlock]
    resp = {
        'signature':     tx.signature.hex(),
        'senderAddress': tx.senderAddress.hex(),
        'coins':         sum([txo.amount for txo in tx.outputs]),
        'inputs': [
            {
                'inTxBlockID': txi.blockID,
                'inTxIndex':   txi.indexInBlock,
                'amount':      find(
                    nbc.blockchain.blocks[txi.blockID].txs[txi.indexInBlock].outputs,
                    lambda txo: txo.address == tx.senderAddress
                )[1].amount
            }
            for txi in tx.inputs
        ],
        'outputs': [
            {
                'address': txo.address.hex(),
                'amount':  txo.amount
            }
            for txo in tx.outputs
        ]
    }
    return resp

@hug.get()
@usingNBC
def connectToNeighbor(nbc, host:str, port:int):
    nbc.runAsync(nbc.node.connectToNeighbor(host, port))
    return {'result': True}

@hug.get()
@usingNBC
def disconnectNeighbor(nbc, guid:str):
    ok = True
    try:
        guid = bytes.fromhex(guid)
        _, n = find(nbc.node.neighbors, lambda n: n.guid == guid)
        n.disconnect()
    except ValueError:
        ok = False
    return {'result': ok}

@hug.get()
@usingNBC
def sendCoins(nbc, address:str, amount:int):
    tx = nbc.createTransaction(bytes.fromhex(address), amount)
    ok = bool(tx) and nbc.enqueTransaction(tx)
    if ok:
        nbc.broadcastTransaction(tx)
    return {'result': ok}
