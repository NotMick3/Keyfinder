# Bitcoin Address Finder

Questo progetto cerca un indirizzo Bitcoin specifico in un intervallo di chiavi private.

## Requisiti

Assicurati di avere installato quanto segue:

- Python 3.8 o successivo
- Moduli Python: `ecdsa`, `Crypto`, `hashlib`, `base58`

Puoi installare i moduli necessari usando il seguente comando:

```bash
pip install ecdsa pycryptodome base58
```
How to Use
Required Modifications

In the Python script, you need to modify the following values to suit your needs:

    target_address: Replace this with the Bitcoin address you are looking for.
    range_start_hex and range_end_hex: Replace these with the range of private keys in hexadecimal format you want to search.

Here is an example of the values you need to modify:

python

# Modify here
target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
range_start_hex = "0000000000000000000000000000000000000000000000030000000000000000"
range_end_hex = "000000000000000000000000000000000000000000000003ffffffffffffffff"

Running the Script

To run the script and start searching for the specific Bitcoin address, open a terminal and navigate to the directory where the script is located, then execute the following command:

bash

python script_name.py

Be sure to replace script_name.py with the actual name of the script file.
Results

The script will print the results of the search to the console, including the corresponding private key in hexadecimal if the target address is found.