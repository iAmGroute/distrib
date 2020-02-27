
import asyncio

from Common.SlotMap  import SlotMap
from NetworkProtocol import NetworkProtocol
from Neighbor        import Neighbor
from Blockchain      import Blockchain

class NbcNode:

    def __init__(self, host, port):
        self.host       = host
        self.port       = port
        self.neighbors  = SlotMap()
        self.blockchain = Blockchain.load('blockchain.txt')
        self.loop       = None

    def runForever(self):
        self.loop = asyncio.new_event_loop()
        self.loop.create_task(self.runServer())
        self.loop.create_task(self.main())
        self.loop.run_forever()

    async def runServer(self):
        await self.loop.create_server(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=self.host, port=self.port,
            reuse_address=True
        )
        print('Server running')

    def connectToNeighbor(self, host, port):
        self.loop.create_task(self.loop.create_connection(
            lambda: NetworkProtocol(self.newConnectionMade),
            host=host, port=port
        ))

    def newConnectionMade(self, link):
        peerName = link.transport.get_extra_info('peername')
        print('New connection:', peerName)
        neighbor      = Neighbor(self, -1, link)
        neighbor.myID = self.neighbors.append(neighbor)

    async def main(self):
        while True:
            await asyncio.sleep(4)
            for neighbor in self.neighbors:
                neighbor.getLatestBlockID()

