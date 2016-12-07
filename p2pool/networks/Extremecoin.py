from p2pool.bitcoin import networks

PARENT = networks.nets['Extremecoin']
SHARE_PERIOD = 15 # seconds target spacing
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares coinbase maturity
SPREAD = 10 # blocks
IDENTIFIER = '5F08D07F3EB0ced0'.decode('hex')
PREFIX = '75AD675C0064ced0'.decode('hex')
P2P_PORT = 29966
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 8970
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
