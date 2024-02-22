def get_vowel_count(s):
    """

    Args:
        s:

    Returns:
    >>> get_vowel_count("this is a certified hood classic")
    """
    if s == '':
        return 0
    elif s[0] in 'AEIOUaeiou':
        # the return of each time it matches is 1 because it simplifies to 0 matches and 1 is added on each time there
        # is a match as it recurs back up, its honestly easier to think of it executing backwards as compared to how it
        # actually executes
        return 1 + get_vowel_count(s[1:])
    else:
        return get_vowel_count(s[1:])


print(get_vowel_count('PalmTree'))


def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)


print(multiply(1.1, 5))


def deep_reverse(a):
    if a == []:
        return []
    else:
        last_el_list = [a[-1]]
        if type(last_el_list[0]) == list:
            rest_reversed = deep_reverse(a[:-1])
            last_el_reversed = deep_reverse(last_el_list[0])
            res = last_el_reversed + rest_reversed
        else:
            rest_reversed = deep_reverse(a[:-1])
            res = last_el_list + rest_reversed
    return res


print(deep_reverse([1, [2, 3], 4]))

# if empty list, return empty list
# if last element not list, return last element in a list + rest elements reversed
# else return last element reversed + rest elements reversed