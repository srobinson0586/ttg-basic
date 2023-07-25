# Python Competency 2 Decryption - README

## Objectives

This competency will help the student utilize all the skills and topics that they have learned since the last competency. After completing this comptency, students will be comfortable with:

- [Numbers](../1.09_numbers/README.md)
- [Strings](../1.10_strings/README.md)
- [Typecasting](../1.11_typecasting/README.md)
- [Lists, Tuples, and Sets](../1.12_lists_tuples_and_sets/README.md)
- [Dictionaries](../1.13_dictionaries/README.md)


## Decryption with Vigenere, Substitution, and One-Time Pad

Your task is to implement three functions that perform decryption/decoding using different ciphers. The provided functions are `decode_vigenere_cipher`, `decode_substitution_cipher`, and `decode_one_time_pad`. Additionally, you need to implement the `combine_ciphers` function that combines the decryption process of all three methods.

TODO: CHANGE "VIGENERE" TO SUM ELSE

1. Implement the `decode_vigenere_cipher` function:
- This function takes two parameters: `ciphertext` (a string) and `vigenere_key` (a string).
- The function performs the decryption by applying the Vigenere cipher algorithm in reverse.
- Each character of the ciphertext is shifted back by the corresponding character from the Vigenere key.
- Non-alphabetic characters are left unchanged.
- It should return the decrypted plaintext obtained after applying the Vigenere cipher algorithm in reverse.

2. Implement the `decode_substitution_cipher` function:
- This function takes two parameters: `ciphertext` (a string) and `substitution_key` (a dictionary).
- The `substitution_key` dictionary represents the substitution key where each key-value pair corresponds to the original character and its substitution character, respectively.
- Return the decrypted string obtained after replacing characters according to the substitution key.

3. Implement the `decode_one_time_pad` function:
- This function takes two parameters: `ciphertext` (a string) and `one_time_pad_key` (a string).
- Each character in the `ciphertext` is XORd with its corresponding character in `one_time_pad_key`. The key is rolled over, used repeatedly until every character in `ciphertext` has been XORd.
- Return the decrypted string obtained by performing XOR decryption with the one-time pad key.

4. Implement the `combine_ciphers` function:
- This function decodes a given `vigenere_ciphertext` using the `decode_vigenere_cipher` function and `vigenere_key` to get a Vigenere plaintext.
- That Vigenere plaintext is then used as the *ciphertext* in a Substitution Cipher, that is decoded with a given `substitution_key` and the `decode_substitution_cipher` function to get a Substitution plaintext.
- Finally, that Substitution plaintext is used as the key to decrypt the encoded `otp_encoded` string using `decode_one_time_pad`.
- Ensure that you have implemented the previous three functions correctly before working on this function.
- Return the decrypted string obtained after the combination of ciphers.

## Resources

- [Vigenere Cipher](https://www.youtube.com/watch?v=SkJcmCaHqS0)
    - Keep in mind that this competency requires you do the opposite (decryption) of what the video shows.
- [String Methods](https://www.w3schools.com/python/python_ref_string.asp)
- [Typecasting](../1.11_typecasting/typecasting.md)
