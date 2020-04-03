
import asyncio
import random

from .Generic         import find
from .SlotMap         import SlotMap
from .Neighbor        import Neighbor
from .NetworkProtocol import NetworkProtocol

class Node:

    def __init__(self, host, port):
        self.host      = host
        self.port      = port
        self.neighbors = SlotMap()
        self.app       = None

    def setApp(self, app):
        self.app = app

    def removeMe(self, neighborID):
        del self.neighbors[neighborID]

    async def runServer(self):
        await asyncio.get_event_loop().create_server(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=self.host, port=self.port,
            reuse_address=True
        )
        print('Server running')

    async def connectToNeighbor(self, host, port):
        await asyncio.get_event_loop().create_connection(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=host, port=port
        )

    def newConnectionMade(self, link):
        peerName = link.transport.get_extra_info('peername')
        print('New connection:', peerName)
        # Remove if already exists, based on its `peerName` (ip, port)
        try:
            _, existingNeighbor = find(self.neighbors, lambda n: n.peerName == peerName)
        except ValueError:
            pass
        else:
            existingNeighbor.disconnect()
        # Add new neighbor
        neighbor      = Neighbor(self, -1, link, peerName)
        neighbor.myID = self.neighbors.append(neighbor)

    def removeDuplicateNeighbor(self, exclude, guid):
        # Remove a duplicate neighbor, based on its `guid`,
        # can be called by a neighbor, passing its `self` as `exclude`.
        if guid is None:
            return
        try:
            _, existingNeighbor = find(
                self.neighbors,
                lambda n: n is not exclude and n.guid == guid
            )
        except ValueError:
            pass
        else:
            existingNeighbor.disconnect()

    def randomNeighbors(self, k):
        ns = list(self.neighbors)
        k  = min(k, len(ns))
        return random.sample(ns, k)

    def multicast(self, f):
        for neighbor in self.neighbors:
            f(neighbor.rpc)

    def gossip(self, f, k=2):
        for neighbor in self.randomNeighbors(k):
            f(neighbor.rpc)

