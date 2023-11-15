#!/bin/python
# Python Operators - Pytest Suite
import application
from base64 import b64decode

enc_a = b'AAAS1Q=='
enc_b = b'AAFDpA=='
enc_c = b'AAACSQ=='
enc_str_1 = b'dGhpcyBiZSBzdHJpbmcgb25l'
enc_str_2 = b'dGhpcyBiZSBzdHJpbmcgdHdv'
enc_str = b'dGhpcyBiZSBzdHJpbmcgb25ldGhpcyBiZSBzdHJpbmcgdHdvbw=='
enc_str_3 = b'U2FtZUxlbmd0aA=='

def test_operators():
    a = int.from_bytes(b64decode(enc_a))
    b = int.from_bytes(b64decode(enc_b))
    c = int.from_bytes(b64decode(enc_c))
    first = application.multiply_and_divide(a,b,c)
    assert first == (a*b)/c, 'multiply_and_divide; Incorrect return value'
    assert type(first) == float, 'multiply_and_divide; Incorrect return type'
    print('[+] multiply_and_divide Test PASSED')
    
    str_1 = b64decode(enc_str_1).decode()
    str_2 = b64decode(enc_str_2).decode()
    assert application.concatenate_strings(str_1, str_2) == b64decode(enc_str_3).decode(), 'concatenate_strings; Incorrect return value'
    assert application.concatenate_strings(str_1, '') == b64decode(enc_str_1).decode(), 'concatenate_strings; Incorrect return value with same length strings'
    print('[+] concatenate_strings Test PASSED')
