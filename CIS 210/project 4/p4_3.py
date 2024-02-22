# Implement your solution here. Remember to follow the 210 Style guide and PEP8. 
# Include doctests whenever appropriate. Feel free to delete these comments.
# To run your doctests, at the "Console" below, type: python -m doctest p4_3.py -v

def encrypt(msg: str) -> str:
    """
    encrypts a message with the ROT 13 method
    Args:
        msg: (str)
            the message to be encypted
    Returns:
        the encoded message

    >>> encrypt('Do or do not. There is no try.')
    'Qb be qb abg. Gurer vf ab gel.'
    >>> encrypt('Ahoy, there!')
    'Nubl, gurer!'
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    da_message = ""
    for i in range(len(msg)):
        in_alpha = alpha.find(msg[i].lower())
        if in_alpha >= 0:
            if msg[i].isupper():
                if in_alpha + 13 >= 25:
                    da_message += alpha[in_alpha - 13].upper()
                else:
                    da_message += alpha[in_alpha + 13].upper()
            else:
                if in_alpha + 13 >= 25:
                    da_message += alpha[in_alpha - 13]
                else:
                    da_message += alpha[in_alpha + 13]
        elif in_alpha == -1:
            da_message += msg[i]
    return da_message


def decrypt(msg: str) -> str:
    """
    decrypts text encoded via the ROT13 method
    Args:
        msg: (str) text to be decoded
    Returns:
        the decoded text
    >>> decrypt('Qb be qb abg. Gurer vf ab gel.')
    'Do or do not. There is no try.'
    >>> decrypt('Nubl, gurer!')
    'Ahoy, there!'
    """
    alpha = "abcdefghijklmnopqrstuvwxyz"
    og_msg = ""
    for i in range(len(msg)):
        in_alpha = alpha.find(msg[i].lower())
        if in_alpha >= 0:
            if msg[i].isupper():
                if in_alpha + 13 >= 25:
                    og_msg += alpha[in_alpha - 13].upper()
                else:
                    og_msg += alpha[in_alpha + 13].upper()
            else:
                if in_alpha + 13 >= 25:
                    og_msg += alpha[in_alpha - 13]
                else:
                    og_msg += alpha[in_alpha + 13]
        elif in_alpha == -1:
            og_msg += msg[i]
    return og_msg


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
