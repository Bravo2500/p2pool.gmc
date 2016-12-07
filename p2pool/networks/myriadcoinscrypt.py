from p2pool.bitcoin import networks

PARENT=networks.nets['myriadcoinscrypt']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 60 # blocks
IDENTIFIER = 'fafa54457667eeef'.decode('hex')
PREFIX = 'fa6754ee45ee76fb'.decode('hex')
P2P_PORT=29978
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=8878
BOOTSTRAP_ADDRS='nz.p2pool.geek.nz:5557 uk.p2pool.geek.nz:5557 birdspool.no-ip.org:5557'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-mir'
VERSION_CHECK=lambda v: True

