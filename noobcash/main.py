'''Noobcash v0.0.01'''

import hug
import json
import threading

import NbcAPI

from NBC   import NBC
from Miner import Miner

from Common.Node import Node

# Temporary for debug
from Common.Rerepl import rerepl


# Configure HUG to send CORS header
api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=10))


def keepRerepl(context):
    while True:
        try:
            rerepl(context, '127.0.0.1', 6202)
            # break
        except OSError as e:
            print(repr(e))


def main(host, port, blockchainFile, keyFile):
    # Init the Node (server)
    node  = Node(host, port)
    # Init the app-specific parts (blockchain, wallet and miner)
    miner = Miner()
    nbc   = NBC(blockchainFile, keyFile, node, miner)
    # Init the REST API (user interface)
    NbcAPI.init(nbc)
    # The Node, Miner and API part must run concurrently,
    # so we run each in its own thread.
    threading.Thread(target=nbc.runForever,   args=(), daemon=True).start()
    threading.Thread(target=miner.runForever, args=(), daemon=True).start()
    threading.Thread(target=keepRerepl,       args=({'nbc': nbc},), daemon=True).start()


# Configure HUG to serve the static files found in '../webui/public'
@hug.static('/')
def staticFilesDir():
    return ('../webui/public',)

# As for the API, we will route it all below '/api',
# so the rest of '/' will be the webui pages.
hug.API(__name__).extend(NbcAPI, '/api')


# Arguements come from config file (can't use sys.argv)
config = json.loads(open('config.json').read())
main(config['host'], config['port'], config['blockchainFile'], config['keyFile'])

