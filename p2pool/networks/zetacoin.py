from p2pool.bitcoin import networks

PARENT = networks.nets['zetacoin']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 12*60*60//20 # shares
REAL_CHAIN_LENGTH = 12*60*60//20 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 100 # blocks
IDENTIFIER = 'fee2135c7a81bddd'.decode('hex')
PREFIX = 'ccc22f181efcd444'.decode('hex')
P2P_PORT = 29935
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8920
BOOTSTRAP_ADDRS = '146.185.171.176:9174 79.2.130.60:9174 23.253.81.150:9174 p2pool-eu.gotgeeks.com p2pool-us.gotgeeks.com rav3n.dtdns.net doge.dtdns.net pool.hostv.pl p2pool.org p2pool.gotgeeks.com p2pool.dtdns.net solidpool.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-zet'
VERSION_CHECK = lambda v: True
