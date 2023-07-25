#!/bin/python
# Python Typecasting - Application

# 1. Take the integer argument and convert it to a 4-byte, little endian, bytes object; return the object
def to_bytes(num: int):
    return num.to_bytes(4, 'little')

# 2. Take the binary, utf-8 encoded argument and convert it to a string; return the string
def to_string(bin: bytes):
    return bin.decode()

# 3. Take the 4 arguments and create a dictionary from them; return the dictionary
# return should look something like {key_1: val_1, key_2: val_2}
def to_dict(key_1, val_1, key_2, val_2):
    return {key_1 : val_1, key_2 : val_2}