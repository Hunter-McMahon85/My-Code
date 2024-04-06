#include <string>
#include <iostream>
#include <vector>
#include "kcipher.h"
#include <cctype>
/* Helper function definitions
 */

string no_space(const string& str)
{
    string result;
    int len = str.length();
    for (int i=0; i<len; i++) 
    {
	char c = LOWER_CASE(str[i]);
	if(find_pos(DEFAULT_ALPHA, c) < ALPHABET_SIZE) 
	{
            result += c;
        }
    }
    return result;
}

bool is_valid(string keyword)
{
	// checks if a given keyword is valid
	int length = keyword.length();
        bool valid = true;
        if (length <= 0)
        {
                valid = false;
        }
        for (int i = 0; i<length; i++)
        {
                // 32 is ascii for space
                if ((find_pos(DEFAULT_ALPHA, keyword[i])>ALPHABET_SIZE) && (int(keyword[i])!=32))
                {
                        valid = false;
                        break;
                } 
        }
	return valid;
}
// -------------------------------------------------------
// Running Key Cipher implementation
// -------------------------------------------------------
struct KCipher::CipherCheshire {
    string cipher_alpha;
    vector <string> book;
    unsigned int page;
};

KCipher::KCipher()
{
	smile = new CipherCheshire;
	string default_key(MAX_LENGTH, 'a');
	smile->book.push_back(default_key);
	smile->page = 0;
	smile->cipher_alpha = DEFAULT_ALPHA;
}

KCipher::KCipher(string title)
{	
	// adds the page to the book without any whitespace
	if (is_valid(title))
        {
		smile = new CipherCheshire;
		smile->book.push_back(no_space(title));
		smile->page = 0;
		smile->cipher_alpha = DEFAULT_ALPHA;
	} else {
                cout<<"Invalid Running Key: "<<title<< endl;
                exit(EXIT_FAILURE);
        }

}

KCipher::~KCipher()
{
	delete smile;
}

void KCipher::add_key(string new_page)
{	
	// adds the page to the book without any whitespace
	if (is_valid(new_page))
        {
		smile->book.push_back(no_space(new_page));
	} else {
		cout<<"Invalid Running Key: "<<new_page << endl;
                exit(EXIT_FAILURE);	
	}
}

void KCipher::set_id(unsigned int page_num)
{
	if (page_num < smile->book.size())
	{	
		smile->page = page_num;
	} else {
		cout<<"Warning: invalid id: "<<page_num<<endl;
		exit(EXIT_FAILURE);
	}
}

string KCipher::encrypt(string raw)
{
	// base encypt but some modifications since cipher_alpha rotates for each one
	cout << "Encrypting...";
	string retStr;
        int len = raw.length();
	// page index aka the index of the current char for the page
        int p_index = 0;
        retStr = raw;
        // decryption loop
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
			// maintain the page index
                        p_index ++;
			if (p_index == smile->book[smile->page].length())
			{
				p_index = 0;
			}
                } else {
                        // if its a space or special char
                        retStr[i] = raw[i];
                }
        }
        cout << "Done" << endl;
        return retStr;
}

string KCipher::decrypt(string enc)
{
	// base decrpyt but some modifications since cipher_alpha changes on for each one
	string retStr;
    	cout << "Decrypting...";
    	int len = enc.length();
	// page index aka the index of the current char for the page
	int p_index = 0;
    	retStr = enc;
	// decryption loop
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
			// maintain p_index
			p_index ++;
			if (p_index == smile->book[smile->page].length())
                        {
                                p_index = 0;
                  	}
		} else {
			// if its a space or special char
			retStr[i] = enc[i];
		}
    	}
    	cout << "Done" << endl;
	return retStr;
}
