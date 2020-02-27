
import hug

node = None

def init(myNode):
    global node
    node = myNode

@hug.get()
def status():
    global node
    resp = {
        'host': node.host,
        'port': node.port,
        'neighbors': [
            {
                'connected':   neighbor.connected,
                'lastBlockID': neighbor.lastBlockID
            }
            for neighbor in node.neighbors
        ],
        'blockchain': [
            block.toJson()
            for block in node.blockchain.blocks
        ]
    }
    return resp

@hug.get()
def save():
    global node
    node.blockchain.save()
    return {'result': True}

@hug.get()
def connectToNeighbor(host:str, port:int):
    global node
    node.connectToNeighbor(host, port)
    return {'return': True}

