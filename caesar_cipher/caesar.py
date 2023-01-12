import nltk
from nltk.corpus import words, names


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


word_list = words.words()
name_list = names.words()

"""
ord(char) changes letter -> number
chr(num) changes number -> letter

A - 65
Z - 90
a - 97
z - 122

- encrypt(‘abc’,1) would return ‘bcd’
- encrypt(‘abc’, 10) would return ‘klm’
- shifts that exceed 26 should wrap around
  - encrypt(‘abc’,27) would return ‘bcd’
"""


def encrypt(plaintext, key):
    string = ""

    for char in plaintext:

        if char.islower():
            keyed = ord(char) + key
            if keyed > 122 or keyed < 97:
                difference = keyed - 123
                modulo = difference % 26
                string += chr(97 + modulo)
            else:
                string += chr(keyed)

        elif char.isupper():
            keyed = ord(char) + key
            if keyed > 90 or keyed < 65:
                difference = keyed - 91
                modulo = difference % 26
                string += chr(65 + modulo)
            else:
                string += chr(keyed)
        else:
            string += char

    return string


def decrypt(encryptedText, key):
    return encrypt(encryptedText, -key)


def crack(encrypted_string):

    encrypted_words_list = encrypted_string.split()
    highest_word_count = 0
    most_probable_key = 0

    for x in range(1, 26):

        count = 0
        for word in encrypted_words_list:
            if decrypt(word, x) in word_list or decrypt(word, x) in name_list:  # name_list - line 90
                count += 1

        if count > highest_word_count:
            highest_word_count = count
            most_probable_key = x

    probability = highest_word_count / len(encrypted_words_list) * 100
    decrypted_word = decrypt(encrypted_string, most_probable_key)

    print(f"Decryption Probability: {probability}%")
    print(f"Most Probable Key: {most_probable_key}")
    return decrypted_word


if __name__ == "__main__":

    real_sentence = "It was the best of times, it was the worst of times."
    encrypted = encrypt(real_sentence, 18)

    result6 = crack(encrypted)
    print(result6)
