import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'fcc1b7dc'.decode('hex')
P2P_PORT = 19902
ADDRESS_VERSION = 21
RPC_PORT = 9902
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'catcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'CAT'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CatCoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Catcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.catcoin'), 'catcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://cat.smartchain.cc/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://cat.smartchain.cc/address/'
TX_EXPLORER_URL_PREFIX = 'http://cat.smartchain.cc/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
