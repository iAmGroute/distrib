# Advertise a transaction to our neighbor.
# `self` is instance of `NeighborRPC`

import json

from Transaction import Transaction

CMD = b'ATX.....'

def request(self, tx):
    data = json.dumps(tx.toJson()).encode('utf-8')
    return self.neighbor.sendRequest(CMD, data, noReply=True)

def respond(self, data):
    if data:
        try:
            tx = Transaction.fromJson(json.loads(data.decode('utf-8')))
        except json.JSONDecodeError:
            return None
        else:
            with self.nbc as nbc:
                nbc.enqueTransaction(tx)
    return None

def process(self, data):
    # pylint: disable=unused-argument
    assert False

