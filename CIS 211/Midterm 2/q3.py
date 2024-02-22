"""
Hunter McMahon
CIS 211
Midterm 2
question 3 submission
"""
from typing import List


# TODO: Midterm 2 Question 3 Matrix class implementation
class Matrix:
    def __init__(self, dimension: int):
        """
        initiator function for the matrix function
        :param dimension: int that determines the size of the matrix
        """
        self.dimension = dimension
        self.data = []
        for i in range(dimension):
            row_list = []
            for j in range(dimension):
                row_list.append(0)
            self.data.append(row_list)

    def __str__(self) -> str:
        """
        string representation of the matrix
        :return: string of the matrix
        """
        matrix_str = ""
        string_data = []
        for i in range(self.dimension):
            row_list = []
            for j in range(self.dimension):
                row_list.append(str(self.data[i][j]))
            string_data.append(row_list)
        for i in range(self.dimension):
            row_str = " ".join(string_data[i]) + '\n'
            matrix_str += row_str
        return matrix_str

    def set_value(self, i: int, j: int, val: int):
        """
        sets the value of a specified matrix entry
        :param i: column int (0-index)
        :param j: row int (0-index)
        :param val: value to insert
        :return: void just modifies self.data
        """
        self.data[j][i] = val

    def is_positive(self) -> bool:
        """
        checks to see if all numbers in the matrix are positive
        :return: true or false depending on weather or not there is a negative number in the matrix
        """
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.data[i][j] <= 0:
                    return False
        return True

    def get_diagonal(self) -> List[int]:
        """
        creates a list of the diagonal for the matrix
        :return: a list of int in the diagonal row of the matrix
        """
        diag_list = []
        for i in range(self.dimension):
            diag_list.append(self.data[i][i])
        return diag_list

    def one_norm(self) -> int:
        """
        computes the one norm int of the matrix which is the max value of the sum of columns absolute value
        :return: the one_norm value of the matrix as an int
        """
        columns = [[] for i in range(self.dimension)]
        for i in range(self.dimension):
            for j in range(self.dimension):
                columns[j].append(abs(self.data[i][j]))
        for i in range(self.dimension):
            columns[i] = sum(columns[i])
        return max(columns)
