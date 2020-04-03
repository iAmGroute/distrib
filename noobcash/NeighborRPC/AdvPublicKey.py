# Advertise our public key (wallet's address) to our neighbor.
# `self` is instance of `NeighborRPC`

CMD = b'APK.....'

def request(self):
    with self.nbc as nbc:
        data = nbc.wallet.address
    return self.neighbor.sendRequest(CMD, data, noReply=True)

def respond(self, data):
    address = data[0:]
    self.neighbor.setGUID(address)
    return None

def process(self, data):
    # pylint: disable=unused-argument
    assert False

