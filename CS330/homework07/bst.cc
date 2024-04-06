#include "bst.h"

// ---------------------------------------
// Node class
// Default constructor
Node::Node() 
{
	// done: Implement this
	this->key = 0;
	this->right = nullptr;
	this->left = nullptr;
	this->parent = nullptr;
}
// Constructor
Node::Node(int in) 
{
	// done: Implement this
	this->key = in;
	this->right = nullptr;
	this->left = nullptr;
	this->parent = nullptr;
}
// Destructor
Node::~Node() 
{
	//done: i dont think we need anything here  Implement this
}

// Add parent 
void 
Node::add_parent(Node* in) 
{
	// done: Implement this
	this->parent = in;
}
// Add to left of current node
void 
Node::add_left(Node* in) 
{
	// done: Implement this
	this->left = in;
}
// Add to right of current node
void 
Node::add_right(Node* in) 
{
	// done: Implement this
	this->right = in;
}

// Get key
int 
Node::get_key()
{
	// done: Implement this
	return this->key;
}

// Get parent node
Node* 
Node::get_parent()
{
	// done: Implement this
	return this->parent;
}

// Get left node
Node* 
Node::get_left()
{
	// done: Implement this
	return this->left;
}

// Get right node
Node* 
Node::get_right()
{
	// done: Implement this
	return this->right;
}
// Print the key to ostream to
// Do not change this
void Node::print_info(ostream& to)
{
    to << key << endl;
}
// ---------------------------------------


// ---------------------------------------
// BST class
// Walk the subtree from the given node
void BST::inorder_walk(Node* in, ostream& to)
{
	// done: Implement this
	if(in != nullptr)
	{
		this->inorder_walk(in->get_left(), to);
		in->print_info(to);
		this->inorder_walk(in->get_right(), to);
	}
}
// Constructor
BST::BST()
{
	// done: Implement this
	this->root = nullptr;
}
// Destructor
BST::~BST()
{
	// done: Implement this
	while (this->root != nullptr)
	{
		this->delete_node(root);
	}
}

// Insert a node to the subtree
void BST::insert_node(Node* in)
{
	// done: Implement this
	Node* y = nullptr;
	Node* x = root;
	while (x != nullptr)
	{
		y = x;
		if (in->get_key() < x->get_key())
		{
			x = x->get_left();
		} else {
			x = x->get_right();
		}
	}
	in->add_parent(y);
	if (y == nullptr)
	{
		root = in;
	} else if (in->get_key() < y->get_key()){
		y->add_left(in);
	}else{
		y->add_right(in);
	}
}

// Delete a node to the subtree
void BST::delete_node(Node* out)
{
	// possibly done: Implement this
        Node * y; 
	Node * x;
	// determine node to splice out
	if ((out->get_left() == nullptr) || (out->get_right() == nullptr))
	{
		y = out;
	} else {
		y = this->get_succ(out);
	}
	// making x a child of y
	if (y->get_left() != nullptr)
	{
		x = y->get_left();
	} else {
		x = y->get_right();
	}
	// splice out y
	if (x != nullptr)
	{
		x->add_parent(y->get_parent());
	} 
	if (y->get_parent() == nullptr)
	{
		root = x;
	} else if (y == y->get_parent()->get_left()) {
		y->get_parent()->add_left(x);
	} else {
		y->get_parent()->add_right(x);
	}
	if (y != out)
	{	
		// copy y's data to z aka out
		Node * holder = new Node(y->get_key());
		holder->add_right(out->get_right());
		holder->add_left(out->get_left());
		holder->add_parent(out->get_parent());
		out = holder;
		delete holder;
	}
	if (y != nullptr)
	{
		delete y;
	}
}

// minimum key in the BST
Node* BST::tree_min()
{
	// potentially don: Implement this
	return this->get_min(this->root);
}
// maximum key in the BST
Node* BST::tree_max()
{
	// potentially done: Implement this
	return this->get_max(this->root);
}
// Get the minimum node from the subtree of given node
Node* BST::get_min(Node* in)
{
	// done: Implement this
	Node* min = in;
	while(min->get_left() != nullptr)
	{
		min = min->get_left();
	}
	return min;
}
// Get the maximum node from the subtree of given node
Node* BST::get_max(Node* in)
{
	// done: Implement this
	Node* max = in;
	while(max->get_right() != nullptr)
	{
		max = max->get_right();
	}
	return max;
}
// Get successor of the given node
Node* BST::get_succ(Node* in)
{
	// done: Implement this
	if (in->get_right() != nullptr)
	{
		return this->get_min(in->get_right());
	}
	Node* y = in->get_parent();
	while ((y != nullptr) and (in == y->get_right()))
	{
		in = y;
		y = y->get_parent();
	}
	return y;
}

// Get predecessor of the given node
Node* BST::get_pred(Node* in)
{
	// done: Implement this
	if (in->get_left() != nullptr)
        {
                return this->get_max(in->get_left());
        }
        Node* y = in->get_parent();
        while ((y != nullptr) and (in == y->get_left()))
        {
                in = y;
                y = y->get_parent();
        }
        return y;
}

// Walk the BST from min to max
void BST::walk(ostream& to)
{
	// done: Implement this
	this->inorder_walk(this->root, to);
}

// Search the tree for a given key
Node* BST::tree_search(int search_key)
{
	// done: Implement this
	Node * x = this->root; 
	while ((x != nullptr) and (search_key != x->get_key()))
	{
		if (search_key < x->get_key())
		{
			x = x->get_left();
		} else { 
			x = x->get_right();
		}
	}
	return x;
}

