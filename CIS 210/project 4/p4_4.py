"""
Hunter McMahon
CIS 210
p4 pt 4
description: secret messages r fun
"""
# Implement your solution here. Remember to follow 210 Style and PEP8.
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run doctests, at the "Console" below, type: python -m doctest p4_4.py -v


from typing import Callable
import p4_1
import p4_2
import p4_3


def encrypt(msg: str, func: Callable[[str], str]) -> str:
    """
    takes a string and encodes it via a given encoding function
    Args:
        msg: (str) string to be encoded
        func: (fun) encoder function string will go through

    Returns:
        the encoded
    >>> encrypt("Ahoy, there!", p4_1.encrypt)
    'hy hr!Ao,tee'
    >>> encrypt("Ahoy, there!", p4_2.encrypt)
    'Aytrh,heo e!'
    >>> encrypt("Ahoy, there!", p4_3.encrypt)
    'Nubl, gurer!'
    """
    return func(msg)


def decrypt(msg: str, func: Callable[[str], str]) -> str:
    """
    takes a string and runs it through an given cypher decryption function
    Args:
        msg: (str) message to be dec
        func: (fun) desired decoder function (for even odd, three rail, or ROT 13

    Returns:
        the result of msg going through the desired cypher
    >>> decrypt("hy hr!Ao,tee", p4_1.decrypt)
    'Ahoy, there!'
    >>> decrypt("Aytrh,heo e!", p4_2.decrypt)
    'Ahoy, there!'
    >>> decrypt("Nubl, gurer!", p4_3.decrypt)
    'Ahoy, there!'
    """
    return func(msg)


def main():
    """Main program to run our encryption/decryption process."""
    cipher = input('Which cipher do you wish to use? ' +
                   '[1=odd/even, 2=three-rail, 3=rot13]? ')
    if cipher == '1':
        encrypt_func = p4_1.encrypt
        decrypt_func = p4_1.decrypt
    elif cipher == '2':
        encrypt_func = p4_2.encrypt
        decrypt_func = p4_2.decrypt
    elif cipher == '3':
        encrypt_func = p4_3.encrypt
        decrypt_func = p4_3.decrypt
    else:
        raise ValueError("Unknown cipher, valid inputs are 1, 2, or 3")

    # Now get the string to encrypt or decrypt
    which = input('Do you wish to encrypt or decrypt a message [E/D]? ')
    if which.upper() == 'E':
        text = input('Enter a line of text to encrypt: ')
        print("Encrypted text:")
        print(encrypt(text, encrypt_func))
    elif which.upper() == 'D':
        text = input('Enter encrypted text to decrypt: ')
        print("Decrypted text:")
        print(encrypt(text, decrypt_func))
    else:
        raise ValueError("Invalid option, I only know E and D!")


if __name__ == '__main__':
    main()
