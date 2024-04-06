#include <string>
#include <iostream>
#include <vector>
#include "kcipher.h"
#include "vcipher.h"

string con_cat(string word, int n)
{
	string ret_str;
	for (int i=0; i<=n; i++)
	{
		ret_str += word;
	}
	return ret_str;
}

// -------------------------------------------------------
// Running Key Cipher implementation
// -------------------------------------------------------
struct VCipher::CipherCheshire {
    string cipher_alpha;
    vector <string> book;
    unsigned int page;
};

VCipher::VCipher()
{
       	smile = new CipherCheshire;
	string default_key(MAX_LENGTH, 'a');
        smile->book.push_back(default_key);
        smile->page = 0;
        smile->cipher_alpha = DEFAULT_ALPHA;
}

VCipher::VCipher(string codeword)
{
        // adds the page to the book without any whitespace
        int length = codeword.length();
	if (length>0)
        {	
		bool no_space = true;
		for (int i = 0; i< length; i++)
		{
			if (find_pos(DEFAULT_ALPHA, codeword[i])>ALPHABET_SIZE)
			{
				no_space = false;
				break;
			}
		}
		if (no_space)
		{
		// first index is different depending on raw/encrypted str len
         	smile = new CipherCheshire;
               	smile->book.push_back(codeword);
		smile->page = 0;
                smile->cipher_alpha = DEFAULT_ALPHA;
		} else {
			cout << "Error: not a valid Vigenere key word" << endl;
                	exit(EXIT_FAILURE);
		}

        } else {
                cout << "Error: Codeword is an empty string" << endl;
                exit(EXIT_FAILURE);
        }
}

VCipher::~VCipher()
{
	delete smile;
}

string VCipher::encrypt(string raw)
{
	// concatinate the codeword until it forms a str longer than the enc string
	string codeword = smile->book[0];
	smile->book[0] = con_cat(codeword, raw.length()/codeword.length());
	// base encypt but some modifications since cipher_alpha rotates for each one
	cout << "Encrypting...";
	string retStr;
        int len = raw.length();
	// page index aka the index of the current char for the page
        int p_index = 0;
        retStr = raw;
        // decryption loop
	if (raw.length() <=  smile->book[smile->page].length())
        {
        	for(int i = 0; i < len; i++)
        	{
                	// genrate the key rotation
                	smile->cipher_alpha = DEFAULT_ALPHA;
                	rotate_string(smile->cipher_alpha, find_pos(DEFAULT_ALPHA, smile->book[smile->page][p_index]));

                	// decode normally; only change should be to increment the page index
                	unsigned int char_pos = find_pos(DEFAULT_ALPHA, raw[i]);
                	if (char_pos < ALPHABET_SIZE)
                	{
                        	// make sure the case is preserved
                        	if (isupper(raw[i]))
                        	{
                                	retStr[i] = UPPER_CASE(smile->cipher_alpha[char_pos]);
                        	} else {
                                	retStr[i] = smile->cipher_alpha[char_pos];
                        	}
                        	p_index ++;
                	} else {
                        	// if its a space or special char
                        	retStr[i] = raw[i];
                	}
        	}
        	cout << "Done" << endl;
	} else {
                cout << "Error: Page Key STR is shorter than RAW STR" << endl;
                exit(EXIT_FAILURE);
        }
        return retStr;
}

string VCipher::decrypt(string enc) 
{
	// concatinate the codeword until it forms a str longer than the enc string
	// decypt it
	string codeword = smile->book[0];
	smile->book[0] = con_cat(codeword, enc.length()/codeword.length());
	// base decrpyt but some modifications since cipher_alpha changes on for each one
	string retStr;
    	cout << "Decrypting...";
    	int len = enc.length();
	// page index aka the index of the current char for the page
	int p_index = 0;
    	retStr = enc;
	// decryption loop
	if (enc.length() <=  smile->book[smile->page].length())
	{
    		for(int i = 0; i < len; i++)
    		{	
			// genrate the key rotation
			smile->cipher_alpha = DEFAULT_ALPHA;
			rotate_string(smile->cipher_alpha, find_pos(DEFAULT_ALPHA, smile->book[smile->page][p_index]));
			// decode normally, just need to update page index
    			unsigned int char_pos = find_pos(smile->cipher_alpha, enc[i]);
			if (char_pos < ALPHABET_SIZE)
			{
				// make sure the case is preserved
	       			if (isupper(enc[i]))
				{
					retStr[i] = UPPER_CASE(DEFAULT_ALPHA[char_pos]);
				} else {
					retStr[i] = DEFAULT_ALPHA[char_pos];
				}
				p_index ++;
			} else {
				// if its a space or special char
				retStr[i] = enc[i];
			}
    		}
    		cout << "Done" << endl;
	} else {
		cout << "Error: Page Key STR is shorter than ENCODED STR" << endl;
       		exit(EXIT_FAILURE);
	}
	return retStr;
}
