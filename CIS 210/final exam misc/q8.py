"""
Final Exam Question 8
CIS 210
Hunter McMahon
Desc: my own personal little enigma machine.... and i think you already know what will be encoded/decoded
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(msg: str, n: int) -> str:
    secret_message = ''
    for i in range(len(msg)):
        in_alpha = alphabet.find(msg[i].lower())
        if in_alpha >= 0:
            if msg[i].isupper():
                if in_alpha + n >= 25:
                    secret_message += alphabet[in_alpha - (25 - (n - 1))].upper()
                else:
                    secret_message += alphabet[in_alpha + n].upper()
            else:
                if in_alpha + n >= n:
                    secret_message += alphabet[in_alpha - (25 - (n - 1))]
                else:
                    secret_message += alphabet[in_alpha + n]
        elif in_alpha == -1:
            secret_message += msg[i]
    return secret_message


def decrypt(msg: str, n: int) -> str:
    original_msg = ""
    for i in range(len(msg)):
        in_alpha = alphabet.find(msg[i].lower())
        if in_alpha >= 0:
            if msg[i].isupper():
                if in_alpha - n >= 0:
                    original_msg += alphabet[in_alpha - n].upper()
                else:
                    original_msg += alphabet[25 - (n - in_alpha-1)].upper()
            else:
                if in_alpha - n >= 0:
                    original_msg += alphabet[in_alpha - n]
                else:
                    original_msg += alphabet[25 - (n - in_alpha-1)]
        elif in_alpha == -1:
            original_msg += msg[i]
    return original_msg


def main():
    print(encrypt('Almost done!', 17))
    print(decrypt('Rcdfjk ufev!', 17))
    print(encrypt('Almost done!', 3))
    print(decrypt('Doprvw grqh!', 3))
    print(encrypt('Never gonna give you up Never gonna let you down Never gonna run around and desert you', 15))
    print(encrypt('Never gonna make you cry Never gonna say goodbye Never gonna tell a lie and hurt you', 15))
    print(decrypt('Ctktg vdccp vxkt ndj je Ctktg vdccp ati ndj sdlc Ctktg vdccp gjc pgdjcs pcs sthtgi ndj', 15))
    print(decrypt('Ctktg vdccp bpzt ndj rgn Ctktg vdccp hpn vddsqnt Ctktg vdccp itaa p axt pcs wjgi ndj', 15))
    # NOBODY EXPECTS RICK ASTLEY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

if __name__ == "__main__":
    main()
