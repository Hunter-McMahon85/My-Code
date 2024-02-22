"""
Hunter McMahon
CIS 210
p4 pt 1
description: this message is: *classified*
"""
# Implement your solution here. Remember to follow the 210 Style guide and PEP8.
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run your doctests, at the "Console" below, type: python -m doctest p4_1.py -v
import doctest


def encrypt(msg: str) -> str:
    """
    encrypts a string by taking away the even and odd characters then re-adds them
    Args:
        msg: (str) string to encrypt

    Returns:
        the encoded string
    >>> encrypt("012")
    '102'
    >>> encrypt("0123")
    '1302'
    """
    odds = ""
    evens = ""
    for i in range(len(msg)):
        even_odd = (i + 1) % 2
        if even_odd == 0:
            evens += msg[i]
        elif even_odd != 0:
            odds += msg[i]
    return evens + odds


def decrypt(msg: str) -> str:
    """
    decrypts a string that was encrypted via the odd_even method
    Args:
        msg:(str) string to be decrypted

    Returns:
    the decrypted message as a string
    >>> decrypt("102")
    '012'
    >>> decrypt("1302")
    '0123'
    """
    og_string = ""
    half_length = int(len(msg) / 2)
    for i in range(half_length):
        if len(msg) % 2 != 0:
            if i == 0:
                og_string += msg[half_length] + msg[i]
            elif i + half_length <= len(msg):
                og_string += msg[i + half_length] + msg[i]
            if len(msg) - 2 <= (i + half_length) <= len(msg) - 1:
                og_string += msg[i + half_length + 1]
        else:
            if i == 0:
                og_string += msg[half_length] + msg[i]
            elif i + half_length <= len(msg):
                og_string += msg[i + half_length] + msg[i]
    return og_string


def main():
    """Main program to run our encryption/decryption process."""

    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(decrypt(text))
    else:
        raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
    main()
