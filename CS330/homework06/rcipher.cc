#include <string>
#include <iostream>
#include "rcipher.h"

// -------------------------------------------------------
// ROT13 Cipher implementation
// -------------------------------------------------------

struct RCipher::CipherCheshire {
    string cipher_alpha;
};

RCipher::RCipher() 
{
	string shift_alpha = DEFAULT_ALPHA;
	rotate_string(shift_alpha, 13);
	smile->cipher_alpha = shift_alpha;
}
