#!/bin/python
# Python Competency 2 Decryption - Pytest Suite
from base64 import b64decode
import decryption

vig_cipher_enc = b'YWxtZ2h4dzQwODc6MWE7Plthc2Q='
vig_key_enc = b'TEVFVENPREU='
vig_plain_enc =  b'cGhpbmZqdDQwODc6MW07Plt3b2s='

sub_cipher_enc = b'c2FpbG9yX3RpbW15'
sub_plain_enc  =  b'eHp1YXE5Mit1YmJe'
sub_key_enc    = {b'cw==': 'x',b'YQ==': 'z',b'aQ==': 'u',b'bA==': 'a',b'bw==': 'q',b'cg==': '9',b'Xw==': '2',b'dA==': '+',b'bQ==': 'b',b'eQ==': '^'}

otp_key_enc = b'MTA0OHhjbWQ7YTMxQF4qQCQrfSJ7'
otp_plain_enc = b'QlFdVBcRMhBSDF5I' 
otp_cipher_enc = b'TkNXREd7TTRTVDNyX2QzQ3JZcFRpMG5fMFAzcjRUMHJ9'

def test_competency_2_decryption():
    # Test decrypt_vigenere_cipher
    vig_key = b64decode(vig_key_enc).decode()
    vig_cipher = b64decode(vig_cipher_enc).decode()
    vig_plain = b64decode(vig_plain_enc).decode()
    assert decryption.decrypt_vigenere_cipher(vig_cipher, vig_key) == vig_plain, "decrypt_vigenere_cipher(): Incorrect return value."
    
    # Test decrypt_substitution_cipher
    sub_cipher = b64decode(sub_cipher_enc).decode()
    sub_plain = b64decode(sub_plain_enc).decode()
    sub_key_dec = {}
    for i in sub_key_enc:
        sub_key_dec.update({b64decode(i).decode():sub_key_enc[i]})
    assert decryption.decrypt_substitution_cipher(sub_cipher, sub_key_dec) == sub_plain, "decrypt_substitution_cipher(): Incorrect return value."

    # Test decrypt_one_time_pad
    otp_key = b64decode(otp_key_enc).decode()
    otp_plain = b64decode(otp_plain_enc).decode()
    assert decryption.decrypt_one_time_pad(sub_cipher, otp_key) == otp_plain, "decrypt_one_time_pad(): Incorrect return value."
    
    # Test combine_ciphers()
    assert decryption.combine_ciphers() == b64decode(otp_cipher_enc).decode()
