
def decrypt_vigenere_cipher(ciphertext, vigenere_key):
    """
    Decrypts a Vigenere cipher encrypted ciphertext using the given Vigenere key.

    The function performs the decryption by applying the Vigenere cipher algorithm in reverse.
    Each character of the ciphertext is shifted back by the corresponding character from the Vigenere key.
    Non-alphabetic characters are left unchanged.
    Lettercase is taken into account (upper/lower), in order to keep the result in the same lettercase. e.g. cipher='a', key='B' == 'z'
    The key will only ever contain alphabetic characters.

    Parameters:
        - ciphertext: str; The encrypted string (ciphertext) to be decrypted using the Vigenere cipher.
        - vigenere_key: str; The key used for decryption, which should have a shorter or equal length
          to the ciphertext. The key is repeated cyclically to match the length of the ciphertext.

    Returns:
        str: The decrypted plaintext obtained after reversing the Vigenere cipher algorithm.

    Example:
    >>> ciphertext = 'almghxw4087:1a;>[asd'
    >>> vigenere_key = 'LEETCODE'
    >>> decrypted_text = decrypt_vigenere_cipher(ciphertext, vigenere_key)
    >>> print(decrypted_text)
    'phinfjt4087:1m;>[wok'
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
        str: The decrypted string obtained after replacing characters according to the substitution key.

    Example:
    >>> ciphertext = 'sailor_timmy'
    >>> substitution_key = {'s': 'x', 'a': 'z', 'i': 'u', 'l': 'a', 'o': 'q', 'r': '9', '_': '2', 't': '+', 'm': 'b', 'y': '^'}
    >>> decrypted_string = decrypt_substitution_cipher(ciphertext, substitution_key)
    >>> print(decrypted_string)
    xzuaq92+ubb^
    """
    # TODO: Implement
    pass

def decrypt_one_time_pad(ciphertext, one_time_pad_key):
    """
    Decrypts an encrypted string using a one-time pad and the given one-time pad key.
    You can assume that len(one_time_pad_key) >= len(ciphertext)

    Parameters:
        - ciphertext: str; The encrypted string to be decrypted.
        - one_time_pad_key: str; The key used for XOR decryption with the encrypted string.
        
    Returns:
        str: The decrypted string obtained by performing XOR decryption with the one-time pad key.
    
    Example:
    >>> ciphertext = 'sailor_timmy'
    >>> one_time_pad_key = '1048xcmd;a31@^*@$+}"{'
    >>> decrypted_string = decrypt_one_time_pad(ciphertext, one_time_pad_key)
    >>> print(decrypted_string)
    'BQ]T\x17\x112\x10R\x0c^H'              (unprintable characters)
    """
    # TODO: Implement
    pass

def combine_ciphers():
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
    vigenere_ciphertext = ">*\".0}AtEWbBP<eZ+yGO1)^nxFi'_&B-p"
    vigenere_key = "NCWDG"
    # TODO: Decrypt Vigenere ciphertext

    # Substitution Cipher using the decrypted vigenere cipher as key
    substitution_key = {'>': 'k', '*': 'w', '"': '6', '.': 'x', '0': '$', '}': ']', 'Y': ')', 'x': '`', 'B': 'j', 'Q': 'w', 'o': 'h', 'Z': '/', 'T': '%', '<': '!', 'y': 't', 'M': '$', '+': "'", 'c': 'o', 'D': '_', 'I': '8', '1': 'D', ')': 'y', '^': '0', 'k': 't', 'r': 'U', 'S': '0', 'g': '{', "'": "'", '_': 'j', '&': '1', 'O': '@', '-': '/', 't': 'P'}
    # TODO: Decrypt substitution ciphertext (vigenere plaintext)

    # One-Time Pad using the decrypted substitution cipher as key
    otp_ciphertext = '%4a<c&dT9#[]zEGgU6/l-I^+e`HU^ep]-'
    # TODO: Decrypt one-time pad ciphertext using OTP key (substitution plaintext)
    
    # TODO: Return the one-time pad plaintext
    return None

# You know when you have the correct hidden message
print("Hidden Message: ", combine_ciphers())
