
import asyncio

from Common.Generic  import find
from Common.SlotMap  import SlotMap
from NetworkProtocol import NetworkProtocol
from Neighbor        import Neighbor
from Blockchain      import Blockchain

class NbcNode:

    def __init__(self, host, port, blockchainFile):
        self.host       = host
        self.port       = port
        self.neighbors  = SlotMap()
        self.blockchain = Blockchain(blockchainFile)
        self.loop       = None

    def removeMe(self, neighborID):
        del self.neighbors[neighborID]

    def runForever(self):
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.runServer())
        self.loop.create_task(self.main())
        self.loop.run_forever()

    def runAsync(self, coroutine):
        self.loop.create_task(coroutine)

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

    async def main(self):
        while True:
            await asyncio.sleep(4)
            for neighbor in self.neighbors:
                neighbor.getLatestBlockID()

