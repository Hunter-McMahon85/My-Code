"""
Hunter McMahon
CIS 211
test_parser.py
Project 4
"""
import unittest
from parser import Parser


class Test_Parse(unittest.TestCase):
    def test_Parse(self):
        """
        test the evaluate function of the add class
        :return: (void)
        """
        self.assertEqual(Parser.parse('5 9 10 * + 6 2 / -'), 92)
        self.assertEqual(Parser.parse('5 9 6 * 5 1 5 + + 4 5 4'), 5)
        self.assertEqual(Parser.parse('9 10 * 5 / 69 +'), 87)
