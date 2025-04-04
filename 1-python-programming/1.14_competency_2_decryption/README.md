# Python Competency 2 - Decryption

[Back to OVERVIEW](../README.md)

Code: [`decryption.py`](./decryption.py)

## Objectives

This competency will help you utilize all the skills and topics you have learned since the last competency. After completing this comptency, you should be comfortable with:

- [Numbers](../1.09_numbers/README.md)
- [Strings](../1.10_strings/README.md)
- [Typecasting](../1.11_typecasting/README.md)
- [Lists, Tuples, and Sets](../1.12_lists_tuples_and_sets/README.md)
- [Dictionaries](../1.13_dictionaries/README.md)


## Decryption Implementation Description

Your task is to implement three functions that perform decryption/decoding using different ciphers. The provided template functions are `decrypt_vigenere_cipher`, `decrypt_substitution_cipher`, and `decrypt_one_time_pad`. You may refer to their docstrings for more details on requirements, but here is the brief for each:

### Vigenere
**`decrypt_vigenere_cipher`**
> Decrypts a Vigenere cipher encrypted ciphertext using the given Vigenere key. The function performs the decryption by applying the Vigenere cipher algorithm in reverse. Each character of the ciphertext is shifted back by the corresponding character from the Vigenere key. Non-alphabetic characters are left unchanged. Lettercase is taken into account (upper/lower), in order to keep the result in the same lettercase. e.g. `cipher='a'`, `key='B'` == `'z'`

### Substitution
**`decrypt_substitution_cipher`**
> Decrypts an encrypted string using a substitution cipher and the given substitution key.

### One-Time Pad
**`decrypt_one_time_pad`**
> Decrypts an encrypted string using a one-time pad and the given one-time pad key.

Additionally, you need to implement the `combine_ciphers` function that combines the decryption process of all three methods.

**`combine_ciphers`**
> This function first decrypts a given `vigenere_ciphertext` using the `decrypt_vigenere_cipher` function and `vigenere_key` to get a Vigenere plaintext. Then that Vigenere plaintext is used as the *ciphertext* in a Substitution Cipher, which is decoded by `decrypt_substitution_cipher` using a given `substitution_key`. Finally, that Substitution plaintext is used as the key to decrypt the encoded `otp_encoded` string using `decrypt_one_time_pad`. Ensure that you have implemented the previous three functions correctly before working on this function. Return the decrypted string obtained after the combination of ciphers.

## Assignment
- [ ] Implement the 4 functions as described above in [`decryption.py`](./decryption.py)
- [ ] Run `pytest` in your current directory. If all test cases pass, you have completed this competency.

## Resources

- [YouTube | Vigenere Cipher](https://www.youtube.com/watch?v=SkJcmCaHqS0)
    - Keep in mind that this competency requires you do the opposite (decryption) of what the video shows.
- [W3Schools | String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [Typecasting](../1.11_typecasting/typecasting.md)

[Back to OVERVIEW](../README.md)
