#include "db.h"
// ---------------------------------------------
// SNode class
// Default constructor
// TODO: Implement this
// BASIC function header is provided for so that the code will compile
// The actual function header may be different 
SNode::SNode() 
{
	num_students ++;

}

// Constructor
// TODO: Implement this
// BASIC function header is provided for so that the code will compile
// The actual function header may be different 
SNode::SNode(string f_, string l_, unsigned int a_) : Node::Node(SNode::num_students)
{
	num_students ++;
	this->first = f_;
	this->last = l_;
	this->age = a_;
}

// Destructor
SNode::~SNode()
{
	// i think done, should be deleted by bst: Implement this
}

unsigned int SNode::num_students = 0;

// Public interface
void SNode::change_first(string f_)
{
	// done: Implement this
	this->first = f_;
} 
void SNode::change_last(string l_)
{
	// done: Implement this
	this->last = l_;
} 
string SNode::get_first()
{
	// done: Implement this
	return this->first;
}
string SNode::get_last()
{
	// done: Implement this
	return this->last;
}

unsigned int SNode::get_age()
{
	// done: Implement this
	return this->age;
}

// Print information about the student
// do not change this
void SNode::print_info(ostream& to)
{
    to << "Student ID: " << this->get_key()
       << "\tFirst: " << this->first
       << "\tLast: " << this->last
       << "\tAge: " << this->age << endl;
}
// ---------------------------------------------
