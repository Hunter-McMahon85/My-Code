"""
Hunter McMahon
CIS211
Lab 6
binary_number.py
"""


class BinaryNumber:
    def __init__(self, bits: list):
        """
        initiator function for the binary number class
        :param bits: an integer list containing only binary numbers (1 and 0)
        """
        self.bit_list = bits

    def __str__(self):
        """
        gives a string to represent an object instance
        :return: the bit_list
        """
        return f"{self.bit_list}"

    def __or__(self, other):
        """

        :return:
        """
        truth_table = []
        for i in range(len(self.bit_list)):
            if self.bit_list[i] or other[i] == 1:
                truth_table.append(1)
            else:
                truth_table.append(0)
        return BinaryNumber(truth_table)

    def __and__(self, other):
        """

        :param other:
        :return:
        """
        truth_table = []
        for i in range(len(self.bit_list)):
            if self.bit_list[i] and other[i] == 1:
                truth_table.append(1)
            else:
                truth_table.append(0)
        return BinaryNumber(truth_table)

    def left_shift(self):
        """
    
        :return: 
        """
        shift_list = []
        for i in range(len(self.bit_list)):
            if i >= len(self.bit_list)-1:
                if self.bit_list[i] == 1:
                    shift_list.append(0)
                else:
                    shift_list.append(1)
            else:
                shift_list.append(self.bit_list[i + 1])
        self.bit_list = shift_list

    def right_shift(self):
        """

        :return:
        """
        shift_list = []
        for i in range(len(self.bit_list)):
            if i == 0:
                if self.bit_list[i] == 1:
                    shift_list.append(0)
                else:
                    shift_list.append(1)
            else:
                shift_list.append(self.bit_list[i - 1])
        self.bit_list = shift_list


if __name__ == '__main__':
    bn = BinaryNumber([1, 0, 1, 0, 1])
    bn2 = BinaryNumber([1, 1, 1, 0, 0])
    print("1st binary number =", bn)

    print("2nd binary number =", bn2)

    print("AND", bn and bn2)

    print("OR", bn or bn2)

    bn.right_shift()
    print("1st number right-shifted =", bn)

    bn.left_shift()
    print("1st number left-shifted =", bn)