#ifndef VCIPHER_H_
#define VCIPHER_H_
//#include "cipher.h"
#include "kcipher.h"

using namespace std;

/* A class that implements a
   Vigenere cipher class. It 
   inherts KCipher */
// done: Implement this class
class VCipher : public KCipher{
        protected: 
    		struct CipherCheshire;
    		CipherCheshire *smile;
	public:
               	VCipher();
               	VCipher(string codeword);
		~VCipher();
	       	virtual string encrypt(string raw) override;
    		virtual string decrypt(string enc) override;
};
#endif

