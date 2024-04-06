#include "cipher.h"
/* Cheshire smile implementation.
   It only contains the cipher alphabet
 */
struct Cipher::CipherCheshire {
    string cipher_alpha;
};

/* This function checks the cipher alphabet
   to make sure it's valid
 */
bool is_valid_alpha(string alpha);


// -------------------------------------------------------
// Cipher implementation
/* Default constructor
   This will actually not encrypt the input text
   because it's using the unscrambled alphabet
 */
Cipher::Cipher()
{
    // DONE: Implement this default constructor
    smile = new CipherCheshire;
    smile->cipher_alpha = DEFAULT_ALPHA; 
}

/* This constructor initiates the object with a
   input cipher key
 */
Cipher::Cipher(string cipher_alpha)
{
    // DONE: Implement this constructor
   	if (is_valid_alpha(cipher_alpha))
   	{
    		smile = new CipherCheshire;
    		smile->cipher_alpha = cipher_alpha;
   	} else {
		cout<<"Invalid cipher alphabet/key: "<<cipher_alpha<<endl;
    		exit(EXIT_FAILURE);
	}	   
}

/* Destructor
 */
Cipher::~Cipher()
{
    // Done
    delete smile;
}

/* This member function encrypts the input text 
   using the intialized cipher key
 */
string Cipher::encrypt(string raw)
{
    cout << "Encrypting...";
    string retStr;
    // done
    // algorithm right, something is not being initialized or stored properly
    retStr = raw; 
    int len = raw.length(); 
    for(int i = 0; i < len; i++)
    {
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
	} else {	
		// if its a space or special char
		retStr[i] = raw[i];
	}
    }
    cout << "Done" << endl;

    return retStr;
}


/* This member function decrypts the input text 
   using the intialized cipher key
 */
string Cipher::decrypt(string enc)
{
    string retStr;
    cout << "Decrypting...";
    // done Finish this function
    int len = enc.length(); 
    retStr = enc;
    for(int i = 0; i < len; i++)
    {
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
	} else {
		// if its a space or special char
		retStr[i] = enc[i];
	}
    }
    cout << "Done" << endl;

    return retStr;

}
// -------------------------------------------------------


//  Helper functions 
/* Find the character c's position in the cipher alphabet/key
 */
unsigned int 
find_pos(string alpha, char c)
{
    	unsigned int pos = 27;

    	// Done
	unsigned int i;
	c = LOWER_CASE(c);
	for(i = 0; i < ALPHABET_SIZE; i++)
	{
		if(alpha[i] == c)
		{		
			pos = i;
			break;
		}
	}
    	return pos;
}

/* Make sure the cipher alphabet is valid - 
   a) it must contain every letter in the alphabet 
   b) it must contain only one of each letter 
   c) it must be all lower case letters 
   ALL of the above conditions must be met for the text to be a valid
   cipher alphabet.
 */
bool is_valid_alpha(string alpha)
{
    bool is_valid = true;
    if(alpha.size() != ALPHABET_SIZE) {
        is_valid = false; 
    } else {
        unsigned int letter_exists[ALPHABET_SIZE];
        for(unsigned int i = 0; i < ALPHABET_SIZE; i++) {
            letter_exists[i] = 0;
        }
        for(unsigned int i = 0; i < alpha.size(); i++) {
            char c = alpha[i];
            if(!((c >= 'a') && (c <= 'z'))) {
                is_valid = false;
            } else {
                letter_exists[(c - 'a')]++;
            }
        }
        for(unsigned int i = 0; i < ALPHABET_SIZE; i++) {
            if(letter_exists[i] != 1) {
                is_valid = false;
            }
        }
    }

    return is_valid;
}
