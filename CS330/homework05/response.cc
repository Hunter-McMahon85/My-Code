/*
  Implementation of methods for classes Response, AngryResponse, HappyResponse
*/
#include <iostream>
#include <string>
#include <algorithm>

#include "response.h"

using namespace std;

/*
  Implementation of Word class
  Don't worry too hard about these implementations.
  If you'd like to learn more about STL see: 
    https://www.geeksforgeeks.org/the-c-standard-template-library-stl/
*/
string Word::upper()
{
  string result(theWord);
  transform(result.begin(), result.end(), result.begin(), ::toupper);
  return result;
}

string Word::lower()
{
  string result(theWord);
  transform(result.begin(), result.end(), result.begin(), ::tolower);
  return result;
}

/*
Implementation of Response methods
*/
bool Response::checkAndRespond(const string& inWord, ostream& toWhere)
{
    	// TODO:
    	// This method should check if the current object's keyword is in the
    	// input message (inWord), and send the proper response to the toWhere
    	// output stream 
    	// String class provides the function 'find' which you might find useful
	
	// https://www.geeksforgeeks.org/string-find-in-cpp/ - was helpful
	bool in_input = inWord.find(Response::keyword.upper())!= string::npos;	
	if (in_input)
	{
		respond(toWhere);
	}	
	return in_input; 
}

void Response::respond(ostream& toWhere)
{
    	// done
    	// This method should 'insert' "I am neither angry nor happy: " followed by
    	// the object's response word to the toWhere output stream, along with
    	// a newline at the end
	toWhere<<"I am neither angry nor happy: "<<Response::response<<endl;
}


void AngryResponse::respond(ostream& toWhere)
{
  	// done
  	// Implement the 'respond' member function for the AngryResponse class so that
  	// the angry rseponse "I am angry: " followed by the object's response word 
  	// is inserted to the toWhere output stream, along with a newline at the end
	toWhere<<"I am angry: "<<Response::response<<endl;
}


/*
  Implementation of HappyResponse methods
*/
void 
HappyResponse::respond(ostream& toWhere)
{
	// done
	// Implement the 'respond' member function for the HappyResponse class so that
	// the happy rseponse "I Am Happy: " followed by the object's response word 
	// is inserted to the toWhere output stream, along with a newline at the end
	toWhere<<"I am happy: "<<Response::response<<endl;
}
