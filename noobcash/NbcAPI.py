
import hug

# pylint: disable=protected-access

nbc = None

def init(nbcInstance):
    global nbc
    nbc = nbcInstance

@hug.get()
def status():
    global nbc
    resp = {
        'host': nbc.node.host,
        'port': nbc.node.port,
        'neighbors': [
            {
                'connected':    neighbor.connected,
                'peerName':     neighbor.peerName,
                'lastBlockID':  neighbor.rpc.lastBlockID,
                'isSyncing':    neighbor.isSyncing,
                'pendingCount': len(neighbor.futures)
            }
            for neighbor in nbc.node.neighbors
        ],
        'blockchain': [
            block.toJson()
            for block in nbc.blockchain.blocks
        ],
        'utxos': [
            (tx.thisHash.hex(), amount)
            for tx, amount in nbc.wallet.getUTXOs()
        ],
        'balance': nbc.wallet.getBalance()
    }
    return resp

@hug.get()
def save():
    global nbc
    nbc.blockchain.save()
    return {'result': True}

@hug.get()
def connectToNeighbor(host:str, port:int):
    global nbc
    nbc.node.runAsync(nbc.node.connectToNeighbor(host, port))
    return {'result': True}

