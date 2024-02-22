"""
Hunter McMahon
Lab 2
fraction.py
pieces of the pie
"""


def gcd(a, b) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


class Fraction:
    def __init__(self, num: float, den: float):
        self.num = num
        self.den = den
        assert self.num >= 0, "Denominator cannot be 0 and Numerator cannot be negative"
        assert self.den > 0, "Denominator cannot be 0 and Numerator cannot be negative"

    # Magic methods
    def __str__(self) -> str:
        return str(self.num) + '/' + str(self.den)

    def __repr__(self) -> str:
        return "Fraction(" + str(self.num) + ',' + str(self.den) + ")"

    def __mul__(self, other: object) -> str:
        new_num = self.num * other.num
        new_den = self.den * other.den
        return str(new_num) + "/" + str(new_den)

    def __add__(self, other: object) -> str:
        common_den = self.den * other.den
        num_factor_1 = self.num * other.den
        num_factor_2 = self.den * other.num
        added_num = num_factor_1 + num_factor_2
        return str(added_num) + '/' + str(common_den)

    def simplify(self):
        the_gcd = gcd(self.num, self.den)
        self.num = int(self.num / the_gcd)
        self.den = int(self.den / the_gcd)
