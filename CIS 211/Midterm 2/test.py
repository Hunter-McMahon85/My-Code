import unittest

class Test1(unittest.TestCase):

    def test_extract_low(self):
        """Extract low 3 bits"""

        self.assertEqual(low_bits.extract(0b10101010101), 0b101)