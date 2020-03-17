
import asyncio

class NetworkProtocol(asyncio.Protocol):

    def __init__(self, onConnect):
        self.onConnect  = onConnect
        self.higherP    = None
        self.transport  = None
        self.recvBuffer = b''

    def connection_made(self, transport):
        self.transport = transport
        f = self.onConnect
        f(self)

    def data_received(self, data):
        self.recvBuffer += data
        available = len(self.recvBuffer)
        while available >= 4:
            header   = self.recvBuffer[0:4]
            totalLen = int.from_bytes(header, 'little') + 4
            if available < totalLen:
                return
            available -= totalLen
            packet          = self.recvBuffer[4:totalLen]
            self.recvBuffer = self.recvBuffer[totalLen:]
            self.higherP.packetReceived(packet)

    def sendPacket(self, packet):
        header = len(packet).to_bytes(4, 'little')
        self.transport.write(header + packet)

    def disconnect(self):
        self.transport.close()

    def connection_lost(self, exc):
        del self.transport
        del self.recvBuffer
        self.higherP.disconnected()

