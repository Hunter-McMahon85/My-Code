"""
Hunter McMahon
CIS 211
Final Q4
Tree
"""


class Node:
    def __init__(self, value, left_child=None, right_child=None):
        """
        initiator function for the node
        :param value: the value for this node
        :param left_child: the optional left child node class instance
        :param right_child: the optional right child node class instance
        """
        self.value = value
        self.left = left_child
        self.right = right_child

    def __str__(self) -> str:
        """
        returns a string representation of the tree
        :return: string rep of the tree
        """
        if self.left is not None:
            return f"{self.value} ({str(self.left)} {str(self.right)})"
        else:
            return f"{self.value}"

    def compute_height(self) -> int:
        """
        returns the height of the current node.
        The height is the distance of the longest path between a leaf node and the current node
        :return: int for the height of all branches of the tree
        """
        height_l = 1
        height_r = 1
        if self.left is not None:
            height_l += self.left.compute_height()
        if self.right is not None:
            height_r += self.right.compute_height()
        if height_l >= height_r:
            return height_l
        else:
            return height_r

    def pretty_print(self, indent: int):
        """
        prints out a nice copy of the tree
        :param indent: the indent for the leaves
        :return: void function
        """
        space = " "
        string = F"{space * indent}{self.value}: {self.compute_height()}"
        print(string)
        if self.left is not None:
            self.left.pretty_print(indent + 1)
        if self.right is not None:
            self.right.pretty_print(indent + 1)


# example code for main
if __name__ == '__main__':
    tree = Node(3, Node(2, Node(5, Node(7), Node(6)), Node(4)),
                Node(1, Node(0), Node(8)))
    print(tree)
    print("Pretty-printed:")
    tree.pretty_print(indent=0)
