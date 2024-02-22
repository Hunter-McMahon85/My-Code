"""
Hunter McMahon
Project 3 part 1: archimedes method
Source: Based off of example in textbook: "Python Programming in Context" by Bradley Miller et. al.
Description: What exactly is pi, lets have wallis take a guess
"""
import doctest


def pi_wallis(num_pairs: int) -> float:
    """
    Uses wallis method to approx pi by accumulating pairs of numbers
    Args:
        num_pairs: (int) number of pairs 2b used to estimate pi with wallis method

    Returns:
        an approx of pi

    >>> pi_wallis(20)
    3.1035169615392304
    >>> pi_wallis(100)
    3.1337874906281575
    >>> pi_wallis(2000)
    3.1412000771927957
    """
    accume = 1
    num = 2
    for i in range(num_pairs):
        term_l = num / (num-1)
        term_r = num / (num+1)
        accume = accume * term_l * term_r
        num += 2
    # return value of pi which = accume*2
    return accume * 2


print(doctest.testmod())
