import pybtc as __parent__
import pybynd.constants as constants
names = getattr(constants, '__all__', [n for n in dir(constants) if not n.startswith('_')])
[setattr(__parent__, name, getattr(constants, name)) for name in names]

import pybynd.opcodes as opcodes
names = getattr(opcodes, '__all__', [n for n in dir(opcodes) if not n.startswith('_')])
[setattr(__parent__, name, getattr(opcodes, name)) for name in names]

from pybynd.opcodes import *

from pybynd.functions.tools import bytes_from_hex, int_to_var_int
from pybynd.functions.script import op_push_data, decode_script
from pybynd.functions.hash import hash160, sha256
from pybynd.functions.address import  hash_to_address, public_key_to_p2sh_p2wpkh_script
from pybynd.functions.key import (is_wif_valid, private_to_public_key)

PrivateKey = __parent__.PrivateKey
PublicKey = __parent__.PublicKey

class Address():
    """
    The class for Address object.
    :param key: (optional) one of this types allowed:

                - private key WIF format
                - instance of ``PrivateKey``
                - private key HEX encoded string
                - instance of ``PublicKey``

                In case no key specified new Address will be created with random keys.
    :param address_type: (optional) P2PKH, PUBKEY, P2WPKH, P2SH_P2WPKH, by default P2WPKH.
    :param compressed: (optional) if set to True private key corresponding compressed public key,
                       by default set to True. Recommended use only compressed public key.
    :param testnet: (optional) if set to True mean that this private key for testnet Bitcoin network.
    In case instance is created from WIF private key, ``PrivateKey`` or ``PublicKey`` compressed and testnet flags
    already contain in initial key parameter and will be ignored.
    """

    def __init__(self, key=None,
                 address_type="P2WPKH", testnet=False, compressed=True, legacy=False):
        self.legacy = legacy
        if key is None:
            #: instance of ``PrivateKey`` class
            self.private_key = PrivateKey(testnet=testnet,
                                          compressed=compressed)
            #: instance of ``PublicKey`` class
            self.public_key = PublicKey(self.private_key)
            #: flag for testnet network address  (boolean)
            self.testnet = testnet
        if isinstance(key, str) or isinstance(key, bytes):
            key = PrivateKey(key, testnet=testnet, compressed=compressed)
        if isinstance(key, PrivateKey):
            self.private_key = key
            self.testnet = key.testnet
            compressed = key.compressed
            self.public_key = PublicKey(self.private_key)
        elif isinstance(key, PublicKey):
            self.public_key = key
            self.testnet = testnet
            compressed = key.compressed
        if address_type not in ("P2PKH", "PUBKEY", "P2WPKH", "P2SH_P2WPKH"):
            raise TypeError("address type invalid")
        if not compressed:
            if address_type not in ("P2PKH", "PUBKEY", "P2SH"):
                raise TypeError("compressed public key invalid")
        #: flag for testnet network address  (boolean)
        self.type = address_type

        if address_type == "PUBKEY":
            self.pubkey_script = b"%s%s" % (op_push_data(self.public_key.key), OP_CHECKSIG)
            self.pubkey_script_hex = self.pubkey_script.hex()
            #: version of witness program for SEGWIT address (string)
        self.witness_version = 0 if address_type == "P2WPKH" else None
        self.compressed = compressed
        if address_type == "P2SH_P2WPKH":
            #: flag for script hash address (boolean)
            self.script_hash = True
            #: redeeem script, only for P2SH_P2WPKH (bytes)
            self.redeem_script = public_key_to_p2sh_p2wpkh_script(self.public_key.key)
            #: redeeem script HEX, only for P2SH_P2WPKH (string)
            self.redeem_script_hex = self.redeem_script.hex()
            #: address hash
            self.hash = hash160(self.redeem_script)
            self.witness_version = None
        else:
            self.script_hash = False
            self.hash = hash160(self.public_key.key)
        #: address hash HEX (string)
        self.hash_hex = self.hash.hex()
        #: address in base58 or bech32 encoding (string)
        self.address = hash_to_address(self.hash,
                                       script_hash=self.script_hash,
                                       witness_version=self.witness_version,
                                       testnet=self.testnet,
                                       legacy=self.legacy)
        self.address = hash_to_address(self.hash,
                                       script_hash=self.script_hash,
                                       witness_version=self.witness_version,
                                       testnet=self.testnet,
                                       legacy=False)

        if not legacy and self.witness_version is None:
            self.legacy_address = hash_to_address(self.hash,
                                           script_hash=self.script_hash,
                                           witness_version=self.witness_version,
                                           testnet=self.testnet,
                                           legacy=True)
    def __str__(self):
        return self.address

class ScriptAddress():
    def __init__(self, script,
                 testnet=False, witness_version=0, legacy=False):
        self.legacy = legacy
        self.witness_version = witness_version
        self.testnet = testnet
        if isinstance(script, str):
            script = bytes_from_hex(script)
        self.script = script
        self.script_hex = self.script.hex()
        if witness_version is None:
            self.hash = hash160(self.script)
        else:
            self.hash = sha256(self.script)
        self.script_opcodes = decode_script(self.script)
        self.script_opcodes_asm = decode_script(self.script, 1)
        self.address = hash_to_address(self.hash,
                                       script_hash=True,
                                       witness_version=self.witness_version,
                                       testnet=self.testnet,
                                       legacy=self.legacy)

    @classmethod
    def multisig(cls, n, m, public_key_list,
                 testnet=False, witness_version=0, legacy=False):
        """
        The class method for creating a multisig address.
        :param n: count of required signatures (max 15).
        :param m: count of total addresses of participants (max 15).
        :param list address_list: addresses list, allowed types:

                             - bytes or HEX encoded private key
                             - private key in WIF format
                             - PrivateKey instance,
                             - bytes or HEX encoded public key
                             - PublicKey instance

        """
        if n > 15 or m > 15 or n > m or n < 1 or m < 1:
            raise TypeError("invalid n of m maximum 15 of 15 multisig allowed")
        if len(public_key_list) != m:
            raise TypeError("invalid address list count")
        script = bytes([0x50 + n])
        for a in list(public_key_list):
            if isinstance(a, str):
                try:
                    a = bytes_from_hex(a)
                except:
                    if is_wif_valid(a):
                        a = private_to_public_key(a, hex=False)
                    pass
            if isinstance(a, Address):
                a = a.public_key.key
            elif isinstance(a, PublicKey):
                a = a.key
            elif isinstance(a, PrivateKey):
                a = private_to_public_key(a.key)
            if not isinstance(a, bytes):
                raise TypeError("invalid public key list element")
            if len(a) == 32:
                a = private_to_public_key(a)
            if len(a) != 33:
                raise TypeError("invalid public key list element size")
            script += int_to_var_int(len(a)) + a
        script += bytes([0x50 + m]) + OP_CHECKMULTISIG
        return cls(script, testnet=testnet, witness_version=witness_version, legacy=legacy)
