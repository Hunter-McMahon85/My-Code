#ifndef KCIPHER_H_
#define KCIPHER_H_
#include "cipher.h"
#include "ccipher.h"

using namespace std;

const unsigned int MAX_LENGTH = 100;

/* A class that implements a
   Running key cipher class. It 
   inherts class Cipher */
// done: Implement this function
class KCipher : public Cipher{
	protected: 
    		struct CipherCheshire;
    		CipherCheshire *smile;
	public:
		KCipher();
		KCipher(string title_page);
		~KCipher();
		virtual void add_key(string new_page);
		virtual void set_id(unsigned int page_num);
		virtual string encrypt(string raw) override;
    		virtual string decrypt(string enc) override;
};

string no_space(const string& str);
#endif

