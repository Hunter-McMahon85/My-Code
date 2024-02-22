def test(lst: list, item: int) -> int:
    """
    Counts the number of items in a list that are smaller than some value.
    You can assume the list is sorted in ascending order.
    Args:
        lst: list to be searched
        item: item to be searched for
    Returns:
        number of items smaller than item
    def count_smaller(lst: list, item: int) -> int:
    Counts the number of items in a list that are smaller than some value.
    You can assume the list is sorted in ascending order.
    Args:
        lst: list to be searched
        item: item to be searched for
    Returns:
        number of items smaller than item
    >>> test.py([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
    4
    >>> test.py([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
    0
    >>> test.py([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
    5
    >>> test.py([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1)
    0
    """
    if item in lst:
        if lst[0] == item:
            return 0
        else:
            return 1 + test(lst[1:], item)
    else:
        return 0
