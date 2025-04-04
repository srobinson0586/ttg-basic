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
    ciphertext_vigenere = 'YGAWI{D4g4aLr}'
    ciphertext_sub = "xz1AWY=23=!@Y"
    ciphertext_otp = b'6\x0c\x06G0\x1bQ\n'  # Unprintable characters
    vigenere_key = 'LEETCODE'
    sub_key = {
        'x': 'p', 'z': 'y', '1': 't', 'A': 'h', 'W': 'o', 'Y': 'n',
        '=': '_', '2': 'i', '3': 's', '!': 'f', '@': 'u'
    }
    otp_key = 'exg5di4a'
    expected_flag = 'NCWDG{Yahaha!_you_found_me!}'

    result = combine_ciphers(
        ciphertext_vigenere,
        ciphertext_sub,
        ciphertext_otp,
        vigenere_key,
        sub_key,
        otp_key
    )

    assert result == expected_flag, (
        f"combine_ciphers failed!\n"
        f"Expected flag: {expected_flag}\n"
        f"Got: {result}\n"
        f"Make sure all your previous decryption functions are working correctly."
    )


if __name__ == "__main__":
    pytest.main(["-v"])
