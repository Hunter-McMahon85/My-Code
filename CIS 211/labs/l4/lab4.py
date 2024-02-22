"""
Hunter McMahon
CIS 211
Lab 4
Binary Search Tree
"""


class Node:
    def __init__(self, a_value: int):
        self.data = a_value

    def sum_data(self) -> int:
        raise NotImplementedError("Method not implemented in the abstract Node class.")

    def __str__(self):
        pass


class Leaf(Node):
    def sum_data(self):
        return self.data

    def __str__(self):
        print(f"<{self.data}>")


class Internal(Node):
    def __init__(self, a_value, left: Node, right: Node):
        super().__init__(a_value)
        self.data = a_value
        self.left = left
        self.right = right

    def sum_data(self):
        if isinstance(self.left, Internal):
            self.left = self.left.__str__()
        if isinstance(self.right, Internal):
            self.left = self.right.__str__()

    def __str__(self):
        return f"<{self.data},{self.right},{self.left}>"


def main():
    l1 = Leaf(3)
    l2 = Leaf(6)
    l3 = Leaf(9)
    i = Internal(7, l2, l3)
    root = Internal(5, l1, i)
    print(root.sum_data())
    print(root)


if __name__ == '__main__':
    main()
