"""
Hunter McMahon
CIS 211
Midterm Problem 3
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

    def sum_internal(self) -> int:
        """
        sums the internal nodes and returns it
        :return: sum of internal node values.
        """
        total = self.value
        if self.left is not None:
            total += self.left.value
        if self.right is not None:
            total += self.right.value
        return total

    def sum_leaves(self) -> int:
        """
        sums all the values in the leaves
        :return: sum of the leaves
        """
        total = 0
        if self.left is not None:
            total += self.left.sum_internal() - self.left.value
        if self.right is not None:
            total += self.right.sum_internal() - self.right.value
        return total

    def is_full(self) -> bool:
        """
        determines if each node is full of leaves (has 2 leaf nodes)
        :return: Boolean value depending on whether or not the leaves are full
        """
        # we cannot enter a right node without a left one in our case
        if self.left is None:
            if self.right is None:
                return True
        else:
            if self.left is Node:
                if self.right is None:
                    if self.left.is_full():
                        return True
                else:
                    if self.left.is_full() and self.right.is_full():
                        return True
        return False


if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(8)
    n3 = Node(9)
    i12 = Node(3, n1)
    i34 = Node(7, n2, n3)
    root = Node(6, i12, i34)

    print(n1)
    print(root)
    print(root.sum_internal())
    print(root.sum_leaves())
    print(root.is_full())
    print(Node(n1, n2, n3).is_full())
    print(n1.is_full())
