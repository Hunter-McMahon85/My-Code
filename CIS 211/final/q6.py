"""
Hunter McMahon
Cis 211
final q6
base helper
"""


class BaseHelper:
    def __init__(self, bi_string: str, base: int):
        """
        initiator for the base helper
        :param bi_string: the binary string
        :param base: the base of the binary string
        """
        self.bi_num = bi_string
        self.based = base

    def show(self):
        """
        string showing in detail the steps involved in converting the number to base-10.
        :return: string showing the steps involved in converting the number to base-10.
        """
        indent = len(self.bi_num) + 1
        start_of_string = F"{self.bi_num} ="
        line_2 = " " * indent + "="
        line_3 = " " * indent + "="
        line_4 = " " * indent + "="
        for x in range(len(self.bi_num)):
            if x < len(self.bi_num)-1:
                start_of_string = start_of_string + F" ({self.bi_num[x]} * {self.based}^{(len(self.bi_num)-1) - x}) +"
            else:
                start_of_string = start_of_string + F" ({self.bi_num[x]} * {self.based}^{(len(self.bi_num)-1) - x})"
        for x in range(len(self.bi_num)):
            if x < len(self.bi_num)-1:
                line_2 = line_2 + F" ({int(self.bi_num[x])} * {self.based ** ((len(self.bi_num)-1) - x)}) +"
            else:
                line_2 = line_2 + F" ({int(self.bi_num[x])} * {self.based ** ((len(self.bi_num)-1) - x)})"
        for x in range(len(self.bi_num)):
            if x < len(self.bi_num)-1:
                line_3 = line_3 + F" {int(self.bi_num[x]) * self.based ** ((len(self.bi_num)-1) - x)} +"
            else:
                line_3 = line_3 + F" {int(self.bi_num[x]) * self.based ** ((len(self.bi_num)-1) - x)}"
        line_4 = line_4 + F" {int(self.bi_num, self.based)}"
        return start_of_string + "\n" + line_2 + "\n" + line_3 + "\n" + line_4


octal_helper = BaseHelper('25', 8)
print(octal_helper.show())
