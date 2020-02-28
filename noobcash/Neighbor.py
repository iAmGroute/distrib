
import asyncio

from Common.SlotMap import SlotMap

from NeighborRPC import handlers, requests

class Neighbor:

    def __init__(self, node, myID, link, peerName):
        self.node        = node
        self.myID        = myID
        self.link        = link
        link.higherP     = self
        self.peerName    = peerName
        self.connected   = True
        self.lastBlockID = 0
        self.futures     = SlotMap()

    def destroy(self):
        print('Destroy')
        if not self.connected:
            return
        self.connected = False
        for future in self.futures:
            future.cancel()
        self.futures.deleteAll()
        self.node.removeMe(self.myID)

    def disconnected(self):
        print('Disconnected')
        self.destroy()

    def disconnect(self):
        print('Disconnecting')
        self.link.disconnect()

    def packetReceived(self, packet):
        print('Received packet:', packet)
        try:
            reply = self.processPacket(packet)
            if reply:
                self.link.sendPacket(reply)
        except AssertionError:
            self.destroy()

    def processPacket(self, packet):
        assert len(packet) >= 16
        ref     = packet[ 0: 4]
        flags   = packet[ 4: 8]
        cmd     = packet[ 8:16]
        data    = packet[16:]
        handler = handlers.get(cmd)
        assert handler
        isReply = flags == b'R...'
        if not isReply:
            ret = handler.respond(self, data)
            if ret is None:
                reply = None
            else:
                reply  = ref
                reply += b'R...'
                reply += cmd
                reply += ret
        else:
            reqID  = int.from_bytes(ref, 'little')
            future = self.futures[reqID]
            if future:
                del self.futures[reqID]
                try:
                    ret = handler.process(self, data)
                except AssertionError:
                    future.cancel()
                else:
                    future.set_result(ret)
            reply = None
        return reply

    def _prepareRequest(self):
        f = asyncio.Future()
        if self.connected:
            reqID = self.futures.append(f)
            ref   = reqID.to_bytes(4, 'little')
        else:
            f.cancel()
            ref = None
        return f, ref

    def sendRequest(self, cmd, data):
        f, ref = self._prepareRequest()
        if ref:
            packet  = ref
            packet += b'....' # flags
            packet += cmd
            packet += data
            self.link.sendPacket(packet)
        return f

    def getLatestBlockID(self):
        return requests['getLatestBlockID'](self)

