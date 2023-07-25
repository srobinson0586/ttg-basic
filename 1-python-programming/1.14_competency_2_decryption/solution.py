
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
    plaintext = ""
    key_length = len(vigenere_key)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = vigenere_key[i % key_length]

        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            new_char = char

        plaintext += new_char

    return plaintext

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
    decrypted_string = ""
    for char in ciphertext:
        decrypted_string += substitution_key[char]
    return decrypted_string

def decrypt_one_time_pad(ciphertext, one_time_pad_key):
    """
    Decrypts an encrypted string using a one-time pad and the given one-time pad key.
    You can assume len(that one_time_pad_key) >= len(ciphertext)

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
    decrypted_string = ""
    
    for i in range(len(ciphertext)):
        cur_chr = chr(ord(ciphertext[i]) ^ ord(one_time_pad_key[i]))
        decrypted_string += cur_chr
    return decrypted_string

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
    vigenere_decoded = decrypt_vigenere_cipher(vigenere_ciphertext, vigenere_key)
    assert vigenere_decoded == '>*".0}YxBQoZT<yM+cDI1)^krSg\'_&O-t', f"VIGENERE: {vigenere_decoded}"

    # Substitution Cipher using the decrypted vigenere cipher as key
    substitution_key = {'>': 'k', '*': 'w', '"': '6', '.': 'x', '0': '$', '}': ']', 'Y': ')', 'x': '`', 'B': 'j', 'Q': 'w', 'o': 'h', 'Z': '/', 'T': '%', '<': '!', 'y': 't', 'M': '$', '+': "'", 'c': 'o', 'D': '_', 'I': '8', '1': 'D', ')': 'y', '^': '0', 'k': 't', 'r': 'U', 'S': '0', 'g': '{', "'": "'", '_': 'j', '&': '1', 'O': '@', '-': '/', 't': 'P'}
    substitution_ciphertext = vigenere_decoded
    substitution_decoded = decrypt_substitution_cipher(substitution_ciphertext, substitution_key)
    assert substitution_decoded == 'kw6x$])`jwh/%!t$\'o_8Dy0tU0{\'j1@/P', "SUBSTITUTION"
    
    # One-Time Pad using the decrypted substitution cipher as key
    otp_key = substitution_decoded
    otp_encoded = '%4a<c&dT9#[]zEGgU6/l-I^+e`HU^ep]-'
    
    # Decrypt One-Time Pad
    otp_decoded = decrypt_one_time_pad(otp_encoded, otp_key)
    
    return otp_decoded

# exit()

################################################################################
# Helper functions that I used to create the challenge, NOT part of the solution
# Turns out setting up the competency was WAY HARDER than implementing its tasks
# Had to account for printable chars & desired output for next step
################################################################################

def create_XOR_cipher_and_key(resulting_flag):
    '''
    Creates a OTP XOR key and ciphertext when given a desired resulting `resulting_flag`. When cipher is XORd with the out_key, users can get resulting_flag. Both outputs are guaranteed to be printable.
    params:
        - resulting_flag: string; Flag that you wish student to receive upon "decrypting" the output ciphertext
    returns:
        (cipher, out_key); A tuple where cipher is the ciphertext resulting from XORing resulting_flag with the out_key
    '''
    import string, random
    # last 6 aren't that printable
    otp_key = string.printable[:-6]
    # no confusing backslash
    otp_key = otp_key.replace('\\', '')

    # the actual key that we ended up using
    out_key = ""
    # ciphertext
    cipher = ""
    for i in range(len(resulting_flag)):
        new_key_chr = random.choice(otp_key)
        cur_chr = chr(ord(resulting_flag[i]) ^ ord(new_key_chr))
        # otp_key doubles as our printable chars reference
        while cur_chr not in otp_key:
            new_key_chr = random.choice(otp_key)
            # only unique values
            if new_key_chr in cipher:
                continue
            cur_chr = chr(ord(resulting_flag[i]) ^ ord(new_key_chr))
        cipher += cur_chr
        out_key += new_key_chr
    return (cipher, out_key)

def find_sub_key_and_cipher(target_plaintext):
    """
    Finds a 6-element-large dictionary key and ciphertext that result in the given plaintext
    after performing the Vigenere cipher.
    Params:
        - target_plaintext: str; The desired plaintext to be obtained after encryption
    Returns:
        A tuple containing the dictionary key and the corresponding ciphertext
    """
    import string, random
    # last 6 not printable
    printables = string.printable[:-6]
    # no confusing backslash
    printables = printables.replace('\\', '')

    # Define the 6-element dictionary key as a list of lowercase letters
    dictionary_key = {}
    # dicts can only use unique keys
    used_keys = []
    for i in target_plaintext:
        cur_key = random.choice(printables)
        while cur_key in used_keys:
            cur_key = random.choice(printables)

        used_keys.append(cur_key)
        dictionary_key.update({ cur_key : i})
    
    cipher = dictionary_key.keys()
    return dictionary_key, cipher

def vigenere_cipher(plaintext, key):
    """
    Encrypts the plaintext using the Vigenere cipher with the given key.
    Params:
        - plaintext: str; The message to be encrypted
        - key: str; The key to use for encryption
    Returns:
        The ciphertext obtained after applying the Vigenere cipher
    """
    ciphertext = ""
    key_length = len(key)

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % key_length]

        if char.isalpha():
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            new_char = char

        ciphertext += new_char

    return ciphertext

def find_vigenere_ciphertext(key, target_plaintext):
    """
    Finds a Vigenere ciphertext that results in the given target plaintext
    using the provided key.
    Params:
        - key: str; The key to use for encryption
        - target_plaintext: str; The desired plaintext to be obtained after encryption
    Returns:
        The ciphertext obtained after applying the Vigenere cipher with the given key
    """
    return vigenere_cipher(target_plaintext, key)

otp_ciphertext, otp_key = create_XOR_cipher_and_key("NCWDG{M4ST3r_d3CrYpTi0n_0P3r4T0r}")
print(f"\nOTP Ciphertext is: {otp_ciphertext}\nOTPKey is: {otp_key}\n")

sub_target_plaintext = otp_key
sub_key, sub_cipher = find_sub_key_and_cipher(sub_target_plaintext)
sub_cipher = ''.join([i for i in sub_cipher])
sub_plain = "".join([sub_key[i] for i in sub_cipher])

print("SUB Dictionary Key:", sub_key)
print("SUB Ciphertext:", sub_cipher)
assert sub_plain == otp_key

vig_key = "NCWDG"
vig_plain = sub_cipher
vig_cipher = find_vigenere_ciphertext(vig_key, vig_plain)
print("\nVIG Ciphertext:", vig_cipher)

## CONSTRUCTING AS SEEN IN THE FEW LINES ABOVE ##
# Given: otp_plain; Get: otp_cipher, otp_key
# Given: sub_plain(otp_key); Get: sub_key, sub_cipher
# Given: vig_plain(sub_cipher), vig_key(controlled); Get: vig_cipher

## WHAT STUDENT MUST THEN DO ##
# Given: vig_cipher, vig_key; Ret: vig_plain
# Given: sub_cipher(vig_plain), sub_key; Ret: sub_plain
# Given: otp_cipher(sub_plain), otp_key; Ret otp_plain

# I just took the output from a random run (since each run gives different outuput)
# And used its values in combine_ciphers() solution.