"""Extract various program elements from a Python program.
You can use this as a starting point for your lab.
To run it, at the terminal:
python3 lab8.py somefile.py
The example tictactoe.py from week 5 is included,
but you can use any of your python codes. You can even run it
on itself!
"""
from typing import List
import re
import sys  # for command-line arguments
# List of all reserved words in Python
import keyword  # for keyword.kwlist


class ProgramGrabber:
    """A class with several methods for extracting pieces of Python programs"""

    RESERVED = keyword.kwlist

    def __init__(self, source: str):
        """Initialize a grabber object from a Python program source string."""
        self.source = source
        self.int_constants = []
        self.identifiers = []
        self.reserved = []
        self.class_names = []
        self.method_names = []
        self.conditionals = []

    def extract_reserved(self):
        """Extract all reserved words"""
        resword = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.reserved = [m.group(0) for m in resword.finditer(self.source)
                         if m.group(0) in self.RESERVED]

    def extract_identifiers(self):
        """Extract all identifiers from a Python program excluding reserved
words."""
        # TODO: Extra (optional) challenge -- skip comments!
        identifier = re.compile(r'Integer[a-zA-Z_][a-zA-Z0-9_]*')
        self.identifiers = [m.group(0) for m in identifier.finditer(self.source)
                            if m.group(0) not in self.RESERVED]

    def extract_int_constants(self):
        """Extract all integer constants from a Python program."""
        int_const = re.compile(r'Integer[\d]')
        self.int_constants = [m.group(0) for m in int_const.finditer(self.source)
                              if m.group(0) not in self.int_constants]

    def extract_class_names(self):
        """Extract all class names from a Python program"""
        classname = re.compile(r'(\AClass\snames:)[a-zA-Z_][a-zA-Z0-9_]*')
        self.class_names = [m.group(0) for m in classname.finditer(self.source)
                            if m.group(0) not in self.RESERVED]

    def extract_method_names(self):
        """Extract all method names from a Python program"""
        methodname = re.compile(r' TODO ')
        self.method_names = [m.group(0) for m in methodname.finditer(self.source)
                             if m.group(0) not in self.RESERVED]

    def extract_conditionals(self):
        """Extract all conditional expressions from a Python program"""
        condition = re.compile(r' TODO ')
        self.conditionals = [m.group(0) for m in condition.finditer(self.source)
                             if m.group(0) not in self.RESERVED]

    def extract_all(self):
        """Extract all the different things."""
        self.extract_int_constants()
        self.extract_reserved()
        self.extract_identifiers()
        self.extract_class_names()
        self.extract_method_names()
        self.extract_conditionals()

    def print_data(self):
        """Print all the data"""
        print('Integer constants:', self.int_constants)
        print('Reserved words:', self.reserved)
        print('Identifiers:', self.identifiers)
        print('Class names:', self.class_names)
        print('Method names:', self.method_names)
        print('Conditionals:', self.conditionals)

    def print_stats(self):
        """Print some derived metrics from our data."""
        print("Program Stats:")
        print("Number of integer constants:", len(self.int_constants))
        print("Number of classes:", len(self.class_names))
        print("Number of methods:", len(self.method_names))
        if len(self.class_names):
            print(f"Number of methods per class: {len(self.method_names) / len(self.class_names): .2f}")
        if len(self.method_names):
            print(f"Number of conditionals per function:{len(self.conditionals) / len(self.method_names): .2f}")
        print(f"Number of identifiers per function:{len(self.identifiers) / len(self.method_names): .2f}")
        print(f"Fraction of reserved words used:{len(set(self.reserved)) / len(keyword.kwlist): .2f}")


def main():
    if len(sys.argv) > 1:
        # We have at least one command-line argument
        source = open(sys.argv[1]).read()
    else:
        source = open('tictactoe_py.txt').read()
        print("No file name given! Running with tictactoe.py."
              "\nGeneral usage: python lab8.py <filename>")

    prog = ProgramGrabber(source)
    prog.extract_all()
    prog.print_data()
    prog.print_stats()


if __name__ == '__main__':
    main()
