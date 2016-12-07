import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX='af4576ee'.decode('hex')
P2P_PORT=19978
ADDRESS_VERSION=50
RPC_PORT=9978
RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
        'myriadaddress' in (yield bitcoind.rpc_help()) and
        not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 1000*100000000 >> (height + 1)//967680
#BLOCKHASH_FUNC=data.hash256
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD=90 # s
SYMBOL='XMY'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'myriadcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/myriadcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.myriadcoin'), 'myriadcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://insight-myr.cryptap.us/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://insight-myr.cryptap.us/address/'
TX_EXPLORER_URL_PREFIX = 'http://insight-myr.cryptap.us/tx/'
SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.001e8
