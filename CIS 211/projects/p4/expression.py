"""
Hunter McMahon
CIS 211
Project 4
expression.py
Expression and BinOp abstract classes and their concrete subclasses for 
representing integer expressions containing +, -, *, /
"""

import logging

# To suppress DEBUG messages, level = logging.INFO
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('expression.py')


class Expression:
    """The abstract (base) class for all other expression node classes."""

    def __init__(self):
        """
        initiator for the expression
        """
        log.debug(f"{self.__class__.__name__} created")
        pass

    def __str__(self) -> str:
        raise NotImplementedError("__str__() is not implemented")

    def evaluate(self) -> int:
        """
        evaluates self
        :return: void
        """
        raise NotImplementedError("evaluate() is not implemented")


class IntValue(Expression):
    def __init__(self, value):
        """
        initiator function for the IntValue class
        :param value: the integer value
        """
        super().__init__()
        self._value = int(value)

    def evaluate(self) -> int:
        """
        returns the integer value as an int
        :return: the integer value
        """
        return self._value

    def __str__(self) -> str:
        """
        returns the integer as a string
        :return: the integer as a string
        """
        return f'{self._value}'


class BinOp(Expression):
    def __init__(self, right, left):
        """
        initiator function for the BinOp class
        :param right: the left leaf/node (should be an instance of the IntValue class)
        :param left:  the left leaf/node (should be an instance of the IntValue class)
        """
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self) -> str:
        raise NotImplementedError("evaluate() is not implemented")

    def evaluate(self) -> int:
        raise NotImplementedError("evaluate() is not implemented")


class Add(BinOp):
    def __init__(self, right, left):
        """
        initiator for the add class
        :param right: the right integer
        :param left:  the left integer
        """
        super().__init__(right, left)
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        returns a string of the addition expression
        :return: a string of the addition expression
        """
        return f"({self.right} + {self.left})"

    def evaluate(self) -> int:
        """
        evaluates the Addition expression
        :return: the sum of left and right
        """
        return self.left.evaluate() + self.right.evaluate()


class Sub(BinOp):
    def __init__(self, right, left):
        """
        initiator for the sub class
        :param right: the right integer
        :param left:  the left integer
        """
        super().__init__(right, left)
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        returns a string of the subtraction expression
        :return: a string of the subtraction expression
        """
        return f"({self.right} - {self.left})"

    def evaluate(self) -> int:
        """
        evaluates the division expression
        :return: the difference between left and right
        """
        return self.right.evaluate() - self.left.evaluate()


class Div(BinOp):
    def __init__(self, right, left):
        """
        initiator for the div class
        :param right: the right integer
        :param left:  the left integer
        """

        super().__init__(right, left)
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        returns a string of the division expression
        :return: a string of the division expression
        """
        return f"({self.right} / {self.left})"

    def evaluate(self) -> int:
        """
        evaluates the division expression
        :return: the quotient of left and right
        """
        return self.right.evaluate() / self.left.evaluate()


class Mul(BinOp):
    """
    initiator for the mul class
    :param right: the right integer
    :param left:  the left integer
    """

    def __init__(self, right, left):
        super().__init__(right, left)
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """
        returns a string of the multiplication expression
        :return:  a string of the multiplication expression
        """
        return f"({self.right} * {self.left})"

    def evaluate(self) -> int:
        """
        evaluates the multiplication expression
        :return: the product of left and right
        """
        return self.left.evaluate() * self.right.evaluate()
