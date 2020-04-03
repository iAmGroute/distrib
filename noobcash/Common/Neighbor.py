
import asyncio

from .SlotMap import SlotMap

from NeighborRPC import NeighborRPC

class Neighbor:

    def __init__(self, node, myID, link, peerName):
        self.node      = node
        self.myID      = myID
        self.link      = link
        link.higherP   = self
        self.peerName  = peerName
        self.connected = True
        self.futures   = SlotMap()
        self.rpc       = NeighborRPC(self)
        self.guid      = None

    def disconnected(self):
        print('Disconnected')
        if not self.connected:
            return
        self.connected = False
        for future in self.futures:
            future.cancel()
        self.futures.deleteAll()
        self.node.removeMe(self.myID)

    def disconnect(self):
        print('Disconnecting')
        self.link.disconnect()

    def packetReceived(self, packet):
        try:
            reply = self.processPacket(packet)
            if reply:
                self.link.sendPacket(reply)
        except AssertionError:
            self.disconnect()

    def processPacket(self, packet):
        assert len(packet) >= 16
        ref     = packet[ 0: 4]
        flags   = packet[ 4: 8]
        cmd     = packet[ 8:16]
        data    = packet[16:]
        isReply = flags == b'R...'
        # print('Received', cmd, 'reply' if isReply else 'request')
        if not isReply:
            ret = self.rpc.respond(cmd, data)
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
                    ret = self.rpc.process(cmd, data)
                except AssertionError:
                    future.cancel()
                else:
                    future.set_result(ret)
            reply = None
        return reply

    def _prepareRequest(self, noReply):
        f = 0 if noReply else asyncio.Future()
        if self.connected:
            reqID = self.futures.append(f)
            ref   = reqID.to_bytes(4, 'little')
            if noReply:
                # No need to wait for a reply, so remove the `0`,
                # and still the reqID cannot be used by anything else.
                del self.futures[reqID]
        else:
            f.cancel()
            ref = None
        return f, ref

    def sendRequest(self, cmd, data, noReply=False):
        f, ref = self._prepareRequest(noReply)
        if ref:
            packet  = ref
            packet += b'....' # flags
            packet += cmd
            packet += data
            # print('Sending ', cmd)
            self.link.sendPacket(packet)
        return f

    def setGUID(self, guid):
        self.guid = guid
        self.node.removeDuplicateNeighbor(exclude=self, guid=guid)

