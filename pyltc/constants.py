from pybtc.constants import *

MAX_AMOUNT = 8400000000000000

# mainnet
MAINNET_PRIVATE_KEY_BYTE_PREFIX = b'\xb0'

MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '6'
MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'T'

MAINNET_SEGWIT_ADDRESS_PREFIX = 'bynd'
MAINNET_ADDRESS_PREFIX = 'L'
MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX = '3'
MAINNET_SCRIPT_ADDRESS_PREFIX = 'M'

MAINNET_ADDRESS_BYTE_PREFIX = b'\x30'
MAINNET_SCRIPT_ADDRESS_LEGACY_BYTE_PREFIX = b'\x05'
MAINNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x32'
MAINNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x00\x0c\x14\x03'

# testnet

TESTNET_PRIVATE_KEY_BYTE_PREFIX = b'\xef'

TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX = '9'
TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX = 'c'

TESTNET_SEGWIT_ADDRESS_PREFIX = 'tbynd'
TESTNET_ADDRESS_PREFIX = 'm'
TESTNET_ADDRESS_PREFIX_2 = 'n'

TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX = '2'
TESTNET_SCRIPT_ADDRESS_PREFIX = 'Q'

TESTNET_ADDRESS_BYTE_PREFIX = b'\x6f'
TESTNET_SCRIPT_ADDRESS_LEGACY_BYTE_PREFIX = b'\xc4'
TESTNET_SCRIPT_ADDRESS_BYTE_PREFIX = b'\x3a'
TESTNET_SEGWIT_ADDRESS_BYTE_PREFIX = b'\x03\x03\x03\x03\x00\x14\x0c\x14\x03'

ADDRESS_PREFIX_LIST = (MAINNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX,
                       TESTNET_ADDRESS_PREFIX_2,
                       MAINNET_SCRIPT_ADDRESS_PREFIX,
                       MAINNET_SCRIPT_ADDRESS_LEGACY_PREFIX,
                       TESTNET_SCRIPT_ADDRESS_PREFIX,
                       TESTNET_SCRIPT_ADDRESS_LEGACY_PREFIX)

PRIVATE_KEY_PREFIX_LIST = (MAINNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           MAINNET_PRIVATE_KEY_COMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_UNCOMPRESSED_PREFIX,
                           TESTNET_PRIVATE_KEY_COMPRESSED_PREFIX)

# CONSTANTS hierarchical deterministic wallets (HD Wallets)
MAINNET_XPRIVATE_KEY_PREFIX = b'\x04\x88\xAD\xE4'
MAINNET_XPUBLIC_KEY_PREFIX = b'\x04\x88\xB2\x1E'
TESTNET_XPRIVATE_KEY_PREFIX = b'\x04\x35\x83\x94'
TESTNET_XPUBLIC_KEY_PREFIX = b'\x04\x35\x87\xCF'
HARDENED_KEY = 0x80000000
FIRST_HARDENED_CHILD = 0x80000000
PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000000, 0x80000000, 0, 0]
TESTNET_PATH_LEVEL_BIP0044 = [0x8000002C, 0x80000001, 0x80000000, 0, 0]