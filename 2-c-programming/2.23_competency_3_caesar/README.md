# C Programming - Caesar

[Back to Overview](../README.md)

## Objectives

This competency will provide you the opportunity to put all the new skills and topics into practice. 

## Objectives

Create a file encryption/decryption program that uses the Caesar cipher with a key value that the user provides. After encrypting a file, the user should have the option to decrypt the encrypted file back to its original plaintext.

## Caesar Implementation Description

A Caesar cipher is a type of substitution cipher where letters in the alphabet are shifted by a fixed number to produce an encoding alphabet. This encoding alphabet can then be used to convert a message into ciphertext and vice versa.

**Encryption:** The mathematical representation of the encryption formula is: $E_n (x) = (x+n) \mod 26$ where $x$ is the letter and $n$ is the key. For example, a Caesar cipher with a key of 3 would encode A as D, H as K, Z as C, and so on. 

**Decryption:**  The mathematical representation of the decryption formula is: $D_n (x) = (x-n) \mod 26$ where $x$ is the letter and $n$ is the key. If a file was encrypted with a key of 3, it should be decrypted with a key of -3. Using a key of 23 would decode D as A, K as H, C as Z, and so on.

Comparing these two formulas we can see that the only difference is whether or not the key is added or subtracted. If the user selects the decrypt option then the value they enter will need to be negated. Doing this conversion will allow for one function to serve as both the encryption and decryption function.

This function will perform the Caesar cipher algorithm on all of the alphabetical characters (both upper and lower case) in a file with the given key and output the result to a new file. If a character is non-alphabetical like a number or symbol then it can be copied to the new file without alteration.

### Example Caesar Usage:

```bash
$ ./caesar
Choose mode: 1 - Encrypt, 2 - Decrypt
Enter your choice: 1

Enter the name of the input file: input.txt

Enter the name of the output file: output.txt

Enter the key: 3

File encrypted successfully.

$ ./caesar
Choose mode: 1 - Encrypt, 2 - Decrypt
Enter your choice: 2

Enter the name of the input file: output.txt

Enter the name of the output file: decrypted.txt

Enter the key: 3

File decrypted successfully.
```

## Assignment
- [ ] Implement [`caesar.c`](./Caesar.c) with the functionality described above so that it uses the Caesar cipher to encrypt and decrypt a file with a given key.

[Back to Overview](../README.md)