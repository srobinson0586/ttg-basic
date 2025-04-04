import pytest
from decryption import (
    decrypt_vigenere_cipher,
    decrypt_substitution_cipher,
    decrypt_one_time_pad,
    combine_ciphers
)


def test_decrypt_vigenere_cipher():
    """Test the Vigenere cipher decryption with given example"""
    ciphertext = 'YGAWI{D4g4aLr}'
    vigenere_key = 'LEETCODE'
    expected_output = 'NCWDG{P4d4wAn}'

    result = decrypt_vigenere_cipher(ciphertext, vigenere_key)

    assert result == expected_output, (
        f"decrypt_vigenere_cipher failed!\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}\n"
        f"With ciphertext: {ciphertext}, key: {vigenere_key}"
    )


def test_decrypt_substitution_cipher():
    """Test the substitution cipher decryption with given example"""
    ciphertext = "xz1AWY=23=!@Y"
    substitution_key = {
        'x': 'p', 'z': 'y', '1': 't', 'A': 'h', 'W': 'o', 'Y': 'n',
        '=': '_', '2': 'i', '3': 's', '!': 'f', '@': 'u'
    }
    expected_output = "python_is_fun"

    result = decrypt_substitution_cipher(ciphertext, substitution_key)

    assert result == expected_output, (
        f"decrypt_substitution_cipher failed!\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}\n"
        f"With ciphertext: {ciphertext}, key: {substitution_key}"
    )


def test_decrypt_one_time_pad():
    """Test the one-time pad decryption with given example"""
    ciphertext_bytes = b'6\x0c\x06G0\x1bQ\n'  # Unprintable characters
    # Convert to a string where each byte is represented as a character
    ciphertext = ciphertext_bytes.decode('latin1')  # Using latin1 to preserve byte values
    one_time_pad_key = 'exg5di4a'
    expected_output = 'StarTrek'

    result = decrypt_one_time_pad(ciphertext, one_time_pad_key)

    assert result == expected_output, (
        f"decrypt_one_time_pad failed!\n"
        f"Expected: {expected_output}\n"
        f"Got: {result}\n"
        f"With ciphertext: {ciphertext}, key: {one_time_pad_key}"
    )


def test_combine_ciphers():
    """Test the combination of all three ciphers to reveal the flag"""
    # Step 1: Vigenere cipher decryption
    ciphertext_vigenere = 'YGAWI{D4g4aLr}'
    vigenere_key = 'LEETCODE'
    # Result of this should be 'NCWDG{P4d4wAn}'

    sub_key = {
        'x': 'p', 'z': 'y', '1': 't', 'A': 'h', 'W': 'o', 'Y': 'n',
        '=': '_', '2': 'i', '3': 's', '!': 'f', '@': 'u'
    }
    reverse_sub = {v: k for k, v in sub_key.items()}

    # Create a key that when used with the OTP will produce our flag
    otp_key_plain = "SecretKey"  # The key that should be produced by step 2

    # Encode it with the substitution cipher (this becomes our ciphertext_sub)
    ciphertext_sub = ""
    for char in otp_key_plain:
        if char in reverse_sub:
            ciphertext_sub += reverse_sub[char]
        else:
            ciphertext_sub += char


    expected_flag = 'NCWDG{Yahaha!_you_found_me!}'
    # Create OTP ciphertext by XORing with our intermediate key (repeating key if needed)
    ciphertext_otp_chars = []
    for i in range(len(expected_flag)):
        # Use modulo to repeat the key as needed
        key_char = otp_key_plain[i % len(otp_key_plain)]
        # XOR between expected flag char and key char
        xor_result = ord(expected_flag[i]) ^ ord(key_char)
        ciphertext_otp_chars.append(xor_result)

    # Convert to bytes
    ciphertext_otp = bytes(ciphertext_otp_chars)

    result = combine_ciphers(
        ciphertext_vigenere,
        ciphertext_sub,
        ciphertext_otp,
        vigenere_key,
        sub_key,
        otp_key_plain
    )

    assert result == expected_flag, (
        f"combine_ciphers failed!\n"
        f"Got: {result}\n"
        f"Make sure all your previous decryption functions are working correctly.\n"
        f"Remember to follow the pipeline: Vigenere → Substitution → OTP"
    )




if __name__ == "__main__":
    pytest.main(["-v"])
