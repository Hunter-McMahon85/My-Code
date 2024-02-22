"""
Hunter McMahon
CIS211
project 4
test_expression.py
"""
import unittest
import expression


class Test_Add(unittest.TestCase):
    def test_Add(self):
        """
        test the evaluate function of the add class
        :return: (void)
        """
        self.assertEqual(expression.Add(expression.IntValue(4), expression.IntValue(4)).evaluate(), 8)
        self.assertEqual(expression.Add(expression.IntValue(6), expression.IntValue(5)).evaluate(), 11)
        self.assertEqual(expression.Add(expression.IntValue(-5), expression.IntValue(6)).evaluate(), 1)

    def test_Add_print(self):
        """
        test the str function of the add class
        :return: (void)
        """
        self.assertEqual(expression.Add(expression.IntValue(4), expression.IntValue(4)).__str__(), '(4 + 4)')
        self.assertEqual(expression.Add(expression.IntValue(6), expression.IntValue(5)).__str__(), '(6 + 5)')
        self.assertEqual(expression.Add(expression.IntValue(-5), expression.IntValue(6)).__str__(), '(-5 + 6)')


class Test_Sub(unittest.TestCase):
    def test_Sub(self):
        """
        test the evaluate function of the Sub class
        :return: (void)
        """
        self.assertEqual(expression.Sub(expression.IntValue(4), expression.IntValue(4)).evaluate(), 0)
        self.assertEqual(expression.Sub(expression.IntValue(6), expression.IntValue(5)).evaluate(), 1)
        self.assertEqual(expression.Sub(expression.IntValue(-5), expression.IntValue(6)).evaluate(), -11)

    def test_Sub_print(self):
        """
        test the str function of the Sub class
        :return: (void)
        """
        self.assertEqual(expression.Sub(expression.IntValue(4), expression.IntValue(4)).__str__(), '(4 - 4)')
        self.assertEqual(expression.Sub(expression.IntValue(6), expression.IntValue(5)).__str__(), '(6 - 5)')
        self.assertEqual(expression.Sub(expression.IntValue(-5), expression.IntValue(6)).__str__(), '(-5 - 6)')


class Test_Div(unittest.TestCase):
    def test_Div(self):
        """
        test the evaluate function of the div class
        :return: (void)
        """
        self.assertEqual(expression.Div(expression.IntValue(12), expression.IntValue(3)).evaluate(), 4)
        self.assertEqual(expression.Div(expression.IntValue(420), expression.IntValue(10)).evaluate(), 42)
        self.assertEqual(expression.Div(expression.IntValue(8), expression.IntValue(4)).evaluate(), 2)

    def test_Div_print(self):
        """
        test the evaluate function of the Div class
        :return: (void)
        """
        self.assertEqual(expression.Div(expression.IntValue(4), expression.IntValue(4)).__str__(), '(4 / 4)')
        self.assertEqual(expression.Div(expression.IntValue(6), expression.IntValue(5)).__str__(), '(6 / 5)')
        self.assertEqual(expression.Div(expression.IntValue(-5), expression.IntValue(6)).__str__(), '(-5 / 6)')


class Test_Mul(unittest.TestCase):
    def test_Mu(self):
        """
        test the evaluate function of the Mu class
        :return: (void)
        """
        self.assertEqual(expression.Mul(expression.IntValue(4), expression.IntValue(4)).evaluate(), 16)
        self.assertEqual(expression.Mul(expression.IntValue(6), expression.IntValue(9)).evaluate(), 54)
        self.assertEqual(expression.Mul(expression.IntValue(-5), expression.IntValue(6)).evaluate(), -30)

    def test_Mul_print(self):
        """
        test the evaluate function of the Mu class
        :return: (void)
        """
        self.assertEqual(expression.Mul(expression.IntValue(4), expression.IntValue(4)).__str__(), '(4 * 4)')
        self.assertEqual(expression.Mul(expression.IntValue(6), expression.IntValue(5)).__str__(), '(6 * 5)')
        self.assertEqual(expression.Mul(expression.IntValue(-5), expression.IntValue(6)).__str__(), '(-5 * 6)')
