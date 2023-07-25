# Python Competency 2 Decryption - README

## Objectives

This competency will help the student utilize all the skills and topics that they have learned since the last competency. After completing this comptency, students will be comfortable with:

- [Numbers](../1.09_numbers/README.md)
- [Strings](../1.10_strings/README.md)
- [Typecasting](../1.11_typecasting/README.md)
- [Lists, Tuples, and Sets](../1.12_lists_tuples_and_sets/README.md)
- [Dictionaries](../1.13_dictionaries/README.md)


## Decryption with Vigenere, Substitution, and One-Time Pad

Your task is to implement three functions that perform decryption/decoding using different ciphers. The provided template functions are `decrypt_vigenere_cipher`, `decrypt_substitution_cipher`, and `decrypt_one_time_pad`. You may refer to their DocuStrings for more details on requirements, but here is the brief for each:

**`decrypt_vigenere_cipher`**
> Decrypts a Vigenere cipher encrypted ciphertext using the given Vigenere key. The function performs the decryption by applying the Vigenere cipher algorithm in reverse. Each character of the ciphertext is shifted back by the corresponding character from the Vigenere key. Non-alphabetic characters are left unchanged. Lettercase is taken into account (upper/lower), in order to keep the result in the same lettercase. e.g. `cipher='a'`, `key='B'` == `'z'`

**`decrypt_substitution_cipher`**
> Decrypts an encrypted string using a substitution cipher and the given substitution key.

**`decrypt_vigenere_cipher`**
> Decrypts an encrypted string using a one-time pad and the given one-time pad key. You can assume `len(that one_time_pad_key) >= len(ciphertext)`

Additionally, you need to implement the `combine_ciphers` function that combines the decryption process of all three methods.

**`combine_ciphers`**
> This function First decrypts a given `vigenere_ciphertext` using the `decrypt_vigenere_cipher` function and `vigenere_key` to get a Vigenere plaintext. Then that Vigenere plaintext is then used as the *ciphertext* in a Substitution Cipher, that is decoded with a given `substitution_key` and the `decrypt_substitution_cipher` function to get a Substitution plaintext. Finally, that Substitution plaintext is used as the key to decrypt the encoded `otp_encoded` string using `decrypt_one_time_pad`. Ensure that you have implemented the previous three functions correctly before working on this function. Return the decrypted string obtained after the combination of ciphers.


## Resources

- [Vigenere Cipher](https://www.youtube.com/watch?v=SkJcmCaHqS0)
    - Keep in mind that this competency requires you do the opposite (decryption) of what the video shows.
- [String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [Typecasting](../1.11_typecasting/typecasting.md)
