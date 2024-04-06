#include <string>
#include <iostream>
#include <algorithm>
#include "ccipher.h"

// -------------------------------------------------------
// Caesar Cipher implementation


// -------------------------------------------------------

struct CCipher::CipherCheshire {
    string cipher_alpha;
};

// default case; shift by zero, same as sub
CCipher::CCipher() : Cipher() {}

CCipher::CCipher(int shift_by)  
{	
	if (shift_by > 0)
	{
		string shift_alpha = DEFAULT_ALPHA;
		rotate_string(shift_alpha, shift_by);
		smile->cipher_alpha = shift_alpha;
	} else 
	{
		cout<<"Error: Caesar cipher is less than 0"<<endl;
		exit(EXIT_FAILURE);
	}
}

string CCipher::encrypt(string raw)
{
	return Cipher::encrypt(raw);
}

string CCipher::decrypt(string enc) 
{
	return Cipher::decrypt(enc);
}
// Rotates the input string in_str by rot positions
void rotate_string(string& in_str, int rot)
{
    // done (i think): You will likely need this function. Implement it.
    for (int i = 0; i <rot; i++)
    {
	char head = in_str[0];
	in_str.erase(0, 1);
    	in_str.push_back(head);
    }
}
