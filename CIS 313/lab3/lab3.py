class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)

    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)

    def insert(self, data):
        """
        inserts data into the BST
        :param data: an integer to be inserted into the BST
        :return: Void
        """
        travel_down = True
        current_node = self.root
        print("insert")
        if self.root is None:
            travel_down = False
            if type(data) is Node:
                self.root = data
            else:
                self.root = Node(data)

        while travel_down:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    current_node.left.parent = current_node
                    travel_down = False
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    current_node.right.parent = current_node
                    travel_down = False
                else:
                    current_node = current_node.right

    def min(self):
        """
        returns the minimum data value in the BST
        :return:
        Returns the minimum value held in the tree
        Returns None if the tree is empty
        """
        current_node = self.root
        if current_node is not None:
            while current_node.left is not None:
                current_node = current_node.left
        else:
            return None
        return current_node.data

    def max(self):
        """
        returns the maximum data value stored in the BST
        :return:
        Returns the maximum value held in the tree
        Returns None if the tree is empty
        """
        current_node = self.root
        if self.root is not None:
            while current_node.right is not None:
                current_node = current_node.right
        else:
            return None
        return current_node.data

    def __find_node(self, data):
        """
        checks to see if a given node in the tree has a data value equal to the given data value
        and returns the node of that value
        :param data: the integer value we want to check and see if it's in a nodes data attribute
        :return:
        the node object with the specified data value, None if the given data value is not in the tree
        """
        # returns the node with that particular data value else returns None
        current_node = self.root
        fall = True
        if current_node is None:
            fall = False
        while fall:
            if data == current_node.data:
                fall = False
                break
            else:
                if data > current_node.data:
                    if current_node.right is None:
                        current_node = None
                        fall = False
                        break
                    else:
                        current_node = current_node.right
                else:
                    if current_node.left is None:
                        current_node = None
                        fall = False
                        break
                    else:
                        current_node = current_node.left
        return current_node

    def contains(self, data):
        """
        uses __find_node to see if a given data value exist in the BST
        :param data: an integer value that we want to check for in the BST
        :return:
        True: the data value is in the BST
        False: the data value is not in the BST
        """
        if self.__find_node(data) is not None:
            return True
        else:
            return False

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
        helper method implemented using generators
        generator function to create an traversal list of the bst, generated recursively using generators
        :param curr_node:
        the current node we are traversing (user should enter root of tree they want traversed)
        :param traversal_type:
        the type of traversal -
        Tree.PREORDER or 1 - makes a preorder traversal [parent, left, right]
        Tree.INORDER or 2 - makes an inorder traversal [left, parent, right]
        Tree.POSTORDER or 3 - makes a postorder traversal [left, right, right]
        :return:
        a traversal of specified type as a list of the data values at each node
        """
        if curr_node is None:
            return
        else:
            node_1 = None
            node_2 = None
            node_3 = None
            if traversal_type == 1:
                node_1 = curr_node
                node_2 = curr_node.left
                node_3 = curr_node.right
            elif traversal_type == 2:
                node_1 = curr_node.left
                node_2 = curr_node
                node_3 = curr_node.right
            elif traversal_type == 3:
                node_1 = curr_node.left
                node_2 = curr_node.right
                node_3 = curr_node

            if node_1 is not None:
                if node_1 == curr_node:
                    yield node_1.data
                else:
                    yield from self.__traverse(node_1, traversal_type)
            if node_2 is not None:
                if node_2 == curr_node:
                    yield node_2.data
                else:
                    yield from self.__traverse(node_2, traversal_type)
            if node_3 is not None:
                if node_3 == curr_node:
                    yield node_3.data
                else:
                    yield from self.__traverse(node_3, traversal_type)

    def find_successor(self, data):
        """
        Finds the successor node; helper method to implement the delete method but may be called on its own
        If the value specified by data does NOT exist in the tree, a KeyError is raised
        If the right subtree of the node is nonempty,then the successor is just, the leftmost node in the right subtree.
        If the right subtree of the node is empty, then go up the tree until a node that is the left child of its parent
        is encountered. The parent of the found node will be the successor to the initial node.
        :param data: the node we want to find the successor of
        :return: object of successor if found else return None
        """
        try:
            if self.contains(data) is False:
                raise KeyError
            else:
                node = self.__find_node(data)
                if node.right is not None:
                    # right subtree is not empty
                    subtree = Tree()
                    subtree.insert(node.right)
                    subtree.root.left = node.right.left
                    subtree.root.right = node.right.right
                    if subtree.root.right and subtree.root.left is None:
                        return subtree.root
                    else:
                        return self.__find_node(subtree.min())
                else:
                    # right subtree is empty
                    while node.parent is not None:
                        if node == node.parent.left:
                            return node.parent
                        node = node.parent
        except KeyError:
            print("Error: Node does not exist in the BST")
            raise KeyError

    def delete(self, data):
        """
        Finds a given node and deletes it from the BST
        If the value specified  does NOT exist in the tree, then a KeyError is Raised
        :param data: (int) the data value of the node to delete
        :return:
        none, function is void
        """
        try:
            if self.contains(data):
                old_node = self.__find_node(data)
                replacement = self.find_successor(old_node.data)
                if old_node.parent is not None:
                    # True = right child of parent
                    # False = left child of parent
                    side = True
                    if old_node.parent.left == old_node:
                        side = False
                    if old_node.left and old_node.right is not None:
                        # two children
                        self.delete(replacement.data)
                        old_node.data = replacement.data
                    elif old_node.left or old_node.right is not None:
                        # one Child
                        if old_node.left is not None:
                            if side:
                                old_node.parent.right = old_node.left
                            else:
                                old_node.parent.left = old_node.left
                        else:
                            if side:
                                old_node.parent.right = old_node.right
                            else:
                                old_node.parent.left = old_node.right
                    else:
                        # no child
                        if side is True:
                            old_node.parent.right = None
                        else:
                            old_node.parent.left = None
                else:
                    # no parent meaning were at the root
                    if replacement is None:
                        self.root = None
                    else:
                        self.delete(replacement.data)
                        self.root.data = replacement.data
                        self.root.left = old_node.left
                        self.root.right = old_node.right
            else:
                raise KeyError
        except KeyError:
            print("Error: data node specified is either not in the Tree or the Tree is Empty")
            raise KeyError
