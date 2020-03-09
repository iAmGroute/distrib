
import asyncio
import random

from Common.Generic  import find
from Common.SlotMap  import SlotMap
from NetworkProtocol import NetworkProtocol
from Neighbor        import Neighbor

class Node:

    def __init__(self, host, port):
        self.host      = host
        self.port      = port
        self.neighbors = SlotMap()
        self.loop      = None
        self.app       = None

    def setApp(self, app):
        self.app = app

    def removeMe(self, neighborID):
        del self.neighbors[neighborID]

    def runAsync(self, coroutine):
        self.loop.create_task(coroutine)

    def runForever(self):
        self.loop = asyncio.new_event_loop()
        self.runAsync(self.runServer())
        if self.app:
            self.runAsync(self.app.main())
        self.loop.run_forever()

    async def runServer(self):
        await self.loop.create_server(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=self.host, port=self.port,
            reuse_address=True
        )
        print('Server running')

    async def connectToNeighbor(self, host, port):
        await self.loop.create_connection(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=host, port=port
        )

    def newConnectionMade(self, link):
        peerName = link.transport.get_extra_info('peername')
        print('New connection:', peerName)
        existingNeighbor = find(self.neighbors, lambda item: item.peerName == peerName)
        if existingNeighbor is not None:
            existingNeighbor.disconnect()
        neighbor      = Neighbor(self, -1, link, peerName)
        neighbor.myID = self.neighbors.append(neighbor)

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

