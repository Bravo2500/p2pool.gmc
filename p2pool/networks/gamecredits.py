from p2pool.bitcoin import networks

PARENT = networks.nets['gamecredits']
SHARE_PERIOD = 10 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 30 # blocks
#IDENTIFIER = '5a1a4884fb33717d'.decode('hex')
#PREFIX = '878022b63d4b7ea2'.decode('hex')
IDENTIFIER = 'e1e1cacae0e0e1e1'.decode('hex')
PREFIX = 'e1e1cacae0e0e1e1'.decode('hex')
P2P_PORT = 29987
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 8897
BOOTSTRAP_ADDRS = 'gamecredits.p2p.0x0a.nl:40003'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
