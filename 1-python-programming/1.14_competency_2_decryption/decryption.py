#!/bin/python
# Python Competency 2 Decryption

def decrypt_vigenere_cipher(ciphertext, vigenere_key):
    """
    Decrypts a Vigenere cipher encrypted ciphertext using the given Vigenere key.

    The function performs the decryption by applying the Vigenere cipher algorithm in reverse.
    Each character of the ciphertext is shifted back by the corresponding character from the Vigenere key.
    Non-alphabetic characters are left unchanged.
    Do NOT iterate through the key for non-alphabetic characters.
    Lettercase is taken into account (upper/lower), in order to keep the result in the same lettercase. e.g. cipher='a', key='B' == 'z'
    The key will only ever contain alphabetic characters.

    Parameters:
        - ciphertext: str; The encrypted string (ciphertext) to be decrypted using the Vigenere cipher.
        - vigenere_key: str; The key used for decryption, which should have a shorter or equal length
          to the ciphertext. The key is repeated cyclically to match the length of the ciphertext.

    Returns:
        str: The decrypted plaintext obtained after reversing the Vigenere cipher algorithm.

    Example:
    >>> ciphertext = 'YGAWI{D4g4aLr}'
    >>> vigenere_key = 'LEETCODE'
    >>> decrypted_text = decrypt_vigenere_cipher(ciphertext, vigenere_key)
    >>> print(decrypted_text)
    'NCWDG{P4d4wAn}'
    """
    # TODO: Implement
    pass

def decrypt_substitution_cipher(ciphertext, substitution_key):
    """
    Decrypts an encrypted string using a substitution cipher and the given substitution key.

    Parameters:
        - ciphertext: str; The encrypted string to be decrypted.
        - substitution_key: dict; A dictionary representing the substitution key where each key-value pair corresponds to the original character and its substitution character, respectively.

    Returns:
        str: The decrypted string obtained after replacing characters according to the substitution key. If a character is unmapped, leave it unchanged in the output.

    Example:
    >>> ciphertext = "xz1AWY=23=!@Y"
    >>> substitution_key = {'x': 'p', 'z': 'y', '1': 't', 'A': 'h', 'W': 'o', 'Y': 'n', '=': '_', '2': 'i', '3': 's', '!': 'f', '@': 'u'}
    >>> decrypted_string = decrypt_substitution_cipher(ciphertext, substitution_key)
    >>> print(decrypted_string)
    python_is_fun
    """
    # TODO: Implement
    pass

def decrypt_one_time_pad(ciphertext, one_time_pad_key):
    """
    Decrypts an encrypted string using a one-time pad and the given one-time pad key.
    If the key is shorter than the ciphertext, you must repeat the key to decrypt the whole string

    Parameters:
        - ciphertext: str; The encrypted string to be decrypted.
        - one_time_pad_key: str; The key used for XOR decryption with the encrypted string.

    Returns:
        str: The decrypted string obtained by performing XOR decryption with the one-time pad key.

    Example:
    >>> ciphertext = '6\x0c\x06G0\x1bQ\n' (unprintable characters)
    >>> one_time_pad_key = 'exg5di4a'
    >>> decrypted_string = decrypt_one_time_pad(ciphertext, one_time_pad_key)
    >>> print(decrypted_string)
    'StarTrek'
    """
    # TODO: Implement
    pass

def combine_ciphers(vigenere_ciphertext, substitution_ciphertext, otp_encoded, vigenere_key, substitution_key, otp_key):
    """
    Combines the decryption of Vigenere Cipher, Substitution Cipher, and One-Time Pad.

    This function First decrypts a given `vigenere_ciphertext` using the `decrypt_vigenere_cipher` function and `vigenere_key` to get a Vigenere plaintext.
    Then that Vigenere plaintext is then used as the *ciphertext* in a Substitution Cipher, that is decoded with a given `substitution_key` and the `decrypt_substitution_cipher` function to get a Substitution plaintext.
    Finally, that Substitution plaintext is used as the key to decrypt the encoded `otp_encoded` string using `decrypt_one_time_pad`.
    Ensure that you have implemented the previous three functions correctly before working on this function.

    Returns:
        str: The decrypted string obtained after the combination of ciphers.
    """
    # Vigenere Cipher
    # TODO: Decrypt Vigenere ciphertext

    # Substitution Cipher using the decrypted vigenere cipher as key
    # TODO: Decrypt substitution ciphertext (vigenere plaintext)

    # One-Time Pad using the decrypted substitution cipher as key
    # TODO: Decrypt one-time pad ciphertext using OTP key (substitution plaintext)

    # TODO: Print then Return the one-time pad plaintext
