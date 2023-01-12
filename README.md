# Cryptography Lab - Caesar Cipher

Create a method to encrypt a message that can be decrypted when supplied with corresponding key. Also devise a way to decipher the encrypted message even when you do not have the key.

## Author: Domine Scully


## Feature Tasks and Requirements

- Create an encrypt function that takes in a plain text phrase and a numeric shift.
  - the phrase will then be shifted that many letters.
    - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
  - shifts that exceed 26 should wrap around
    - E.g. encrypt(‘abc’,27) would return ‘bcd’
- shifts that push a letter out or range should wrap around
  - E.g. encrypt(‘zzz’,1) would return ‘aaa’
- Create a decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
- create a crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.

## Implementation Notes

- In order to accomplish a certain task you’ll need access to a corpus of English words.
  - A search on something like python list of english words should get you going.

## User Acceptance Tests

- encrypt a string with a given shift
- decrypt a previously encrypted string with the same shift
- encryption should handle upper and lower case letters
- encryption should allow non-alpha characters but ignore them, including white space
- decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
- refer to supplied unit tests.

## How to run

Run file: python caesar_cipher/caesar.py

Run tests: pytest tests/test_caesar.py