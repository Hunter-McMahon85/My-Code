"""
Hunter McMahon
Cis 211
File: parser.py
A postfix expression parser.
"""
import expression

import logging

# To suppress DEBUG messages, level = logging.INFO
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('parser.py')


class Parser:
    """A small parser for reverse polish notation (RPN) calculator
    
    Examples:
        4 2 / is equivalent to (4 / 2)
        1 2 + 3 *  is equivalent to ((1 + 2) * 3)
        5 3 - 2 1 + *  is equivalent to ((5 - 3) * (2 + 1))
        5 3 - 2 1 + / 3 1 - * is equivalent to (((5 - 3) / (2 + 1)) * (3 - 1))
    """
    # You may find this useful once you create the expression classes

    OPS = {
        '+': expression.Add,
        '-': expression.Sub,
        '*': expression.Mul,
        '/': expression.Div
    }

    def __init__(self):
        """Initialize the parser"""
        self.parse_tree = None

    def parse(self, code: str) -> expression.Expression:
        """Parse the given postfix expression code string.
        
        Args: 
            code: a string containing an expression to be parsed
            
        Returns:
            An Expression object representing the root of the 
            parse tree of the expression.
        """
        # Add spaces around parentheses and operators, just in case
        for symbol in self.OPS:
            code = code.replace(symbol, ' ' + symbol + ' ')

        # split the string into individual items
        tokens = code.split()
        # Using an array as a stack to parse the postfix format
        stack = []
        index = 0
        while index < len(tokens):
            # The main steps:
            #   - Append (push) any int values to the stack. 
            #   - When the token is an operator, pop the left and right
            # operands from the stack. 
            #   - Then, create a new node with the operator and the two 
            # operands as children, and push (append) the new node to the stack.
            if tokens[index] in '0123456789':
                stack.append(expression.IntValue(tokens[index]))
                log.debug(f"Integer: {tokens[index]}")
            elif tokens[index] in '+-*/':
                log.debug(f"Binary Operator: {tokens[index]}")
                right = stack.pop()
                left = stack.pop()
                stack.append(self.OPS[tokens[index]](left, right))

            index += 1

        # The tree root should be the only thing in the stack
        if len(stack) != 1:
            raise ValueError("Invalid expression")

        log.debug("Parsed: " + str(stack[0]))
        self.parse_tree = stack[0]
        return stack[0]


if __name__ == '__main__':
    # Local tests
    """ parser = Parser()
    for exp in ('4 2 /', '5 3 - 2 1 + *', '5 3 - 2 1 + / 3 1 - *','5 1 + 2 -'):
        parse_tree = parser.parse(exp)
        log.info(f"{exp} = {parse_tree} = {parse_tree.evaluate()}")
    """
    test = Parser().parse('5 1 + 2 -').evaluate()
    print(test)
