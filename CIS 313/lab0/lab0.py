class mathOps:
    """
    Simple math operations on a given pair of integers, u and v.

    This includes the lcm (least common multiple) and 
    gcd (greatest common divisor) functions, each of returns an integer.
    """

    def __init__(self, u, v):
        """Set the values of u and v to be used in the math operations."""
        self.u = u
        self.v = v

    def __repr__(self):
        return "mathOps({}, {})".format(self.u, self.v)

    def valid(self):
        """True if both u and v are integers."""
        return isinstance(self.u, int) and isinstance(self.v, int)

    def gcd(self):
        """
        Compute the greatest common divisor of member variables u and v.
        """
        # Find the greatest common divisor of a and b
        # Hint: Use Euclid's Algorithm
        # https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure
        tempU = round(self.u)
        tempV = round(self.v)

        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError

            elif tempU == 0:
                if tempV == 0:
                    return 0
                else:
                    return abs(tempV)

            elif tempV == 0:
                if tempU == 0:
                    raise Exception
                else:
                    return abs(tempU)

            else:
                if not self.valid():
                    if not isinstance(self.u, float) and isinstance(self.v, float):
                        raise TypeError
                smallest_entry = None
                abs_tempV = abs(tempV)
                abs_tempU = abs(tempU)
                if abs_tempV < abs_tempU:
                    smallest_entry = abs_tempV
                else:
                    smallest_entry = abs_tempU
                for i in range(smallest_entry + 1):
                    num_2_check = smallest_entry - i
                    if tempU % num_2_check == 0 and tempV % num_2_check == 0:
                        return num_2_check

        except OverflowError:
            print("one or both the values of", tempU, " and ", tempV, "are equal to infinity")
            raise OverflowError
        except TypeError:
            print("at least one entry of", tempU, " and ", tempV, "are of a invalid type")
            raise TypeError

    def lcm(self):
        """Compute the least common multiple of member variables u and v."""
        # Hint: Use the gcd of a and b
        tempU = round(self.u)
        tempV = round(self.v)

        try:
            if tempU == (float("inf") or float("-inf")) or tempV == (float("inf") or float("-inf")):
                raise OverflowError
            else:
                if tempU == 0 or tempV == 0:
                    raise Exception
                else:
                    return abs(tempV * tempU) / (self.gcd())

        except OverflowError:
            print("one or both the values of ", tempU, " and ", tempV, " are equal to infinity")
            raise OverflowError
        except Exception:
            print("both the values of", tempU, " and ", tempV, "are equal to zero")
            raise Exception
