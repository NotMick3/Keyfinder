# Bitcoin Address Finder

This project searches for a specific Bitcoin address within a range of private keys.

![Example](example.gif)


## Requirements

Make sure you have the following installed:

-Python 3.8 or later

-Python module:  bitcoinlib


You can install the required modules using the following command:

```bash
pip install bitcoinlib

```

## Clone the Repository

1. Open a terminal.
2. Run the following command to clone the repository:

    ```bash
    git clone https://github.com/NotMick3/Keyfinder.git
    ```
    
## How to Use

Required Modifications


In the Python script, you need to modify the following values to suit your needs:

```bash
target_address 
range_start_int 
range_end_int
```


Here is an example of the values you need to modify:

```bash
target_address = "13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so"
range_start_int = "0000000000000000000000000000000000000000000000020000000000000000"
range_end_int = "000000000000000000000000000000000000000000000003ffffffffffffffff"
```

## Running the Script

To run the script and start searching for the specific Bitcoin address, open a terminal and navigate to the directory where the script is located, then execute the following command:

```bash

python Keyfinder.py
```


The script will print the results of the search to the console, including the corresponding private key in hexadecimal if the target address is found.