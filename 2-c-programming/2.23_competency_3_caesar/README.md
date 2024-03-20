## Enhancement: File Decryption

Extend the file encryption program to include decryption functionality. After encrypting a file, the user should have the option to decrypt the encrypted file back to its original plaintext.

### Additional Functionality:

1. **Decryption:** Implement a function to decrypt an encrypted file using the same Caesar cipher algorithm but with the inverse key. For example, if a file was encrypted with a key of 3, it should be decrypted with a key of -3 (or 26 - 3 = 23).

2. **User Interaction:** Prompt the user to choose between encryption and decryption modes.

3. **Error Handling:** Handle errors gracefully, such as attempting to decrypt a file that has not been encrypted or providing an incorrect decryption key.

### Example Usage:

```$ ./encrypt
Choose mode:

Encrypt
Decrypt
Enter your choice: 1
Enter the name of the input file: input.txt
Enter the name of the output file: output.txt
Enter the encryption key: 3
File encrypted successfully.

$ ./encrypt
Choose mode:

Encrypt
Decrypt
Enter your choice: 2
Enter the name of the input file: output.txt
Enter the name of the output file: decrypted.txt
Enter the decryption key: 3
File decrypted successfully.```


### Notes:

- Ensure that the decryption function works correctly by decrypting files that were previously encrypted by the program.
- Provide clear instructions to the user on how to choose between encryption and decryption modes and enter the necessary information.
