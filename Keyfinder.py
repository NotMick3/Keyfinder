import random
from bitcoinlib.keys import Key

# Target Bitcoin address
target_address = "1E6NuFjCi27W5zoXg8TRdcSRq84zJeBW3k"

# Range of private keys (in hexadecimal format)
range_start_int = int("0000000000000000000000000000000000000000000000000000000000000010", 16)
range_end_int = int("000000000000000000000000000000000000000000000000000000000000001f", 16)

def find_target_address():
    """
    Search for the target Bitcoin address within the specified range of private keys.
    """
    while True:
        
        random_private_key_int = random.randint(range_start_int, range_end_int)
        private_key_hex = hex(random_private_key_int)[2:].zfill(64)
        key = Key(private_key_hex)
        bitcoin_address = key.address()
        print(f"Examining private key in hexadecimal: {private_key_hex}")
        print(f"Generated Bitcoin address: {bitcoin_address}")
        if bitcoin_address == target_address:
            print(f"\nFound Bitcoin address: {bitcoin_address}")
            print(f"Corresponding private key in hexadecimal: {private_key_hex}")
            return

if __name__ == "__main__":
    find_target_address()
