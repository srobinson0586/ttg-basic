#!/bin/python
# Python Debugging - Application
import pdb

#1. TODO: Use the Python Debugger to analyze and display the value of 'secret' after each loop iteration, 
# then display it again after the loop finishes and 'secret' has been fully formed.

# This script loops each byte of a byte array (msg) and performs an XOR operation to form a secret message (secret).
if __name__ == "__main__":
    msg = b'\x9b\x9a\x9e\x9b\x9d\x9a\x9a\x99'
    secret = bytearray()

    for byte in msg:
        secret.append(byte ^ 0xFF)

    secret = secret.decode()    # What is the value of 'secret' at this point in the script?