"""
Hunter McMahon
CIS 210
p4 pt 2
description: james bond 007 be like
"""
# Implement your solution here. Remember to follow the 210 Style guide and PEP8.
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run your doctests, at the "Console" below, type: python -m doctest p4_2.py -v


def encrypt(msg: str) -> str:
    """
    encrypts via 3 rails method
    Args:
        msg: (str) string to be encrypted
    Returns:
    >>> encrypt('Ahoy, there!')
    'Aytrh,heo e!'
    >>> encrypt('There is no reason anyone would want a computer in their home.')
    'Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m'
    """
    train_1 = ""
    train_2 = ""
    train_3 = ""
    for i in range(0, len(msg), 3):
        train_1 += msg[i]
        if i + 1 <= len(msg) - 1:
            train_2 += msg[i + 1]
        if i + 2 <= len(msg) - 1:
            train_3 += msg[i + 2]
    return train_1 + train_2 + train_3


def decrypt(msg: str) -> str:
    """

    Args:
        msg:

    Returns:
        the decrypted message
    >>> decrypt('Trinrs yeoda cpeitihehesoeoao u naournhro.e   annnwlwt mt  e m')

    >>> decrypt('Aytrh,heo e!')
    'Ahoy, there!'
    """
    og_train = ""
    un_third = int(len(msg) / 3)
    for i in range(un_third):
        if len(msg) % 3 != 0:
            if i == 0:
                og_train += msg[i] + msg[un_third - 1] + msg[2 * un_third + 2]
            elif i + un_third <= len(msg):
                og_train += msg[i] + msg[i + un_third + 1] + msg[i + un_third + un_third + 2]
            # if there is 1 leftover character
            if len(msg) - 2 <= (i + un_third * 2) <= len(msg) - 1:
                og_train += msg[i + 1]
            # if there are 2 leftover characters
            elif len(msg) - 3 <= (i + un_third * 2) <= len(msg) - 1:
                og_train += msg[i + 1] + msg[i + un_third + 2]
        # if the string can be divided by 3:
        else:
            if i == 0:
                og_train += msg[i] + msg[un_third] + msg[2 * un_third]
            elif i + un_third <= len(msg):
                og_train += msg[i] + msg[i + un_third] + msg[i + 2 * un_third]
    return og_train


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
