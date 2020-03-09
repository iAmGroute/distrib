'''Noobcash v0.0.01'''

import hug
import json
import threading

import NbcAPI

from NBC   import NBC
from Node  import Node
from Miner import Miner


# Configure HUG to send CORS header
api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=10))


def main(host, port, blockchainFile, keyFile):
    # Init the Node (server)
    node  = Node(host, port)
    # Init the app-specific parts (blockchain, wallet and miner)
    nbc   = NBC(blockchainFile, keyFile, node)
    miner = Miner(nbc)
    # Init the REST API (user interface)
    NbcAPI.init(nbc)
    # The Node, Miner and API part must run concurrently,
    # so we run each in its own thread.
    threading.Thread(target=node.runForever,  args=(), daemon=True).start()
    threading.Thread(target=miner.runForever, args=(), daemon=True).start()


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

