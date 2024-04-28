import hashlib
import base58
import ecdsa
from Crypto.Hash import RIPEMD160
import random

curve = ecdsa.SECP256k1

# Modify here
target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
range_start_hex = "0000000000000000000000000000000000000000000000030000000000000000"
range_end_hex = "000000000000000000000000000000000000000000000003ffffffffffffffff"


range_start_int = int(range_start_hex, 16)
range_end_int = int(range_end_hex, 16)

def generate_bitcoin_address(private_key_raw):
    """
    Generate a Bitcoin address from a private key in raw (byte) format.

    Args:
        private_key_raw (bytes): Private key on raw format.

    Returns:
        str: Bitcoin address.
    """
    
    sk = ecdsa.SigningKey.from_string(private_key_raw, curve=curve)
    vk = sk.verifying_key
    public_key_raw = vk.to_string()
    sha256_hash = hashlib.sha256(public_key_raw).digest()
    ripemd160_hash = RIPEMD160.new(data=sha256_hash).digest()
    network_prefix = b'\x00'
    payload = network_prefix + ripemd160_hash
    double_sha256 = hashlib.sha256(hashlib.sha256(payload).digest()).digest()
    checksum = double_sha256[:4]
    address_payload = payload + checksum
    bitcoin_address = base58.b58encode(address_payload).decode('utf-8')
    return bitcoin_address

def find_target_address():
    while True:
        
        random_private_key_int = random.randint(range_start_int, range_end_int)
        private_key_raw = random_private_key_int.to_bytes(32, 'big')
        bitcoin_address = generate_bitcoin_address(private_key_raw)
        print(f"Examining private key in hexadecimal: {hex(random_private_key_int)[2:].zfill(64)}")
        print(f"Generated Bitcoin address: {bitcoin_address}")
        if bitcoin_address == target_address:
            print(f"\nFound Bitcoin address: {bitcoin_address}")
            print(f"Corresponding private key in hexadecimal: {hex(random_private_key_int)[2:].zfill(64)}")
            return
        
if __name__ == "__main__":
    find_target_address()
