"""
Hunter McMahon
Mini Project 3
CIS 211
where is waldo? he's pretty elusive, but we know he's hiding in that matrix somewhere
"""

import provided  # some helper functions, feel free to use (or not)
from typing import List  # so we can specify list of list of string argument types

WALDO = 'W'
OTHER = '.'


# user defined Functions


def rotate_matrix(matrix: List[List[str]]) -> List[List[str]]:
    """
    rotates the matrix so that the list are the elements of the columns instead of the rows
    :param matrix: a list of list containing the data
    :return:
    the reorganized list of list of values by column instead of rows
    """
    col_list = [[] for i in range(provided.ncols(matrix))]
    for i in matrix:
        for j in range(provided.ncols(matrix)):
            col_list[j].append(i[j])
    return col_list


# The matrix argument of all functions is a list of lists of strings

# for all, there exists

def all_row_exists_waldo(matrix: List[List[str]]) -> bool:
    """
    For all rows in the matrix, return True if WALDO is in some column on each row
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if a waldo exist in each row in some column
    """
    for i in matrix:
        if WALDO not in i:
            return False
    return True


def all_col_exists_waldo(matrix: List[List[str]]) -> bool:
    """
    For all columns in the matrix, return True if WALDO is in some row of every column
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if a waldo exist in some row of every column
    """
    # puts the values of each column into a list in a list
    col_list = rotate_matrix(matrix)
    # test to see if a waldo is in each column
    for i in col_list:
        if WALDO not in i:
            return False
    return True


# for all, for all
# because of the nature of these tow, the functions are the same for both essentially

def all_row_all_waldo(matrix: List[List[str]]) -> bool:
    """
    For all rows in the matrix, return True if WALDO is in every column of every row
    (we have a matrix of waldos)
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if a waldo exist in every column of every row
    """
    for i in matrix:
        for j in i:
            if j != WALDO:
                return False
    return True


def all_col_all_waldo(matrix: List[List[str]]) -> bool:
    """
    For all the columns in the matrix, return True if WALDO is in every row of every column
    (we have a matrix of waldos)
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if a waldo exist in every row of every column
    """

    for i in matrix:
        for j in i:
            if j != WALDO:
                return False
    return True


# there exists, for all

def exists_row_all_waldo(matrix: List[List[str]]) -> bool:
    """
    Return True if there is some row in the matrix in which WALDO is in every column
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if some row in the matrix has WALDO in every column
    """
    # converts the matrix values into booleans, so we can use any
    tf_list = [provided.is_waldo_list(i, WALDO) for i in matrix]
    # checks to see if all elements in a row are waldo
    for i in tf_list:
        if all(i):
            return True
    return False


def exists_col_all_waldo(matrix: List[List[str]]) -> bool:
    """
    Return True if there is some column in the matrix in which WALDO is in every row
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if some column in the matrix has a WALDO in every row
    """
    # "rotate" the matrix
    col_lst = rotate_matrix(matrix)
    # converts the matrix values into booleans, so we can use any
    tf_list = [provided.is_waldo_list(i, WALDO) for i in col_lst]
    # checks to see if all elements in a column are waldo
    for i in tf_list:
        if all(i):
            return True
    return False


def exists_row_exists_waldo(matrix: List[List[str]]) -> bool:
    """
    Return True if there is some row in the matrix in which WALDO is in some column
    :param matrix: a list of list containing the data strings
    :return:
    a boolean that is True if some row in the matrix has a WALDO in some column
    """
    # converts the matrix values into booleans, so we can use any
    tf_list = [provided.is_waldo_list(i, WALDO) for i in matrix]
    # checks to see if any elements in a row are a waldo
    for i in tf_list:
        if any(i):
            return True
    return False


def exists_col_exists_waldo(matrix: List[List[str]]) -> bool:
    """ Return True if there is some column in the matrix in which WALDO is in some row
        :param matrix: a list of list containing the data strings
        :return:
        a boolean that is True if some column in the matrix has a WALDO in some row
        """
    # "rotate" the matrix
    col_lst = rotate_matrix(matrix)
    # converts the matrix values into booleans, so we can use any
    tf_list = [provided.is_waldo_list(i, WALDO) for i in col_lst]
    # checks to see if any elements in a column are a waldo
    for i in tf_list:
        if any(i):
            return True
    return False
