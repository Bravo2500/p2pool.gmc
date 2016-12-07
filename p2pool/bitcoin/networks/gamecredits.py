import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fbc0b6db'.decode('hex')
P2P_PORT = 19987
ADDRESS_VERSION = 38
RPC_PORT = 9987
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'address' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 90 # s
SYMBOL = 'GMC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'gamecredits') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/gamecredits/') if platform.system() == 'Darwin' else os.path.expanduser('~/.gamecredits'), 'gamecredits.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://159.203.226.245:3000/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://159.203.226.245:3000/address/'
TX_EXPLORER_URL_PREFIX = 'http://159.203.226.245:3000/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
