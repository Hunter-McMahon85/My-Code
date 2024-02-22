"""
Hunter McMahon
CIS 211
Mini project 2
Desc: will i need a broom to sweep this data?
"""
from itertools import groupby


def all_same(lst: list) -> bool:
    """
    determines if all values in a list are the same
    :param lst: (list) the list we are evaluating
    :return:
    (boolean) True/False
    >>> all_same([0, 0, 0])
    True
    >>> all_same([0, 1, 0])
    False
    >>> all_same([])
    True
    """
    all_equal = True
    for i in range(len(lst)):
        if i < len(lst) - 1:
            if lst[i] == lst[i + 1]:
                pass
            else:
                all_equal = False
                break
        elif i == len(lst) - 1:
            if lst[i] == lst[i - 1]:
                pass
            else:
                all_equal = False
                break
    return all_equal


def dedup(lst: list) -> list:
    """
    makes it so that values that repeat and are next to each other are condenced down into 1 value
    :param lst: (list) the list we are deduping/ removing duplicate values from
    :return:
    (list) the input list but with repeating neighboring values condensed into 1 value
    >>> dedup([1, 1, 2, 1, 1, 1])
    [1, 2, 1]
    >>> dedup([])
    []
    """
    # was originally attempting a tedious way via if statements etc. until i got stuck and discovered that this exist
    # https://docs.python.org/3/library/itertools.html#itertools.groupby
    # new_lst = []
    # for i in groupby(lst):
    #    new_lst.append(i[0])
    # return new_lst
    return [i[0] for i in groupby(lst)]


def max_run(lst: list) -> int:
    """
    finds the max run of same numbers in a row in a given list
    :param lst: (list) the list were finidng runs of numbers in
    :return: (int) the length of the longest run
    >>> max_run([1, 1, 2, 2, 3, 4, 4, 4, 2, 4, 4])
    3
    >>> max_run([])
    0
    >>> max_run([1, 2, 3])
    1
    >>> max_run([-2, 0, 0, 1, 2, 1, 1, 1, 0])
    3
    """
    # TODO: implement the function, include a proper docstring
    # Optionally, include doctests (not unittests)
    longest_run = 0
    for i in range(len(lst)):
        run_is_on = True
        tracker = 0
        run_counter = 0
        while run_is_on:
            if i + tracker < len(lst):
                if lst[i + tracker] == lst[i]:
                    run_counter += 1
                    tracker += 1
                else:
                    run_is_on = False
            else:
                run_is_on = False
        if run_counter > longest_run:
            longest_run = run_counter
    return longest_run



if __name__ == "__main__":
    for lst in ([], [1, 1, 1], [1, 4, 4, 4, -2, -2, -2, -2, 3, 1, 4]):
        print(f"1. all_same({lst}) = {all_same(lst)}")
        print(f"2. dedup({lst}) = {dedup(lst)}")
        print(f"3. max_run({lst}) = {max_run(lst)}")
        print("")
