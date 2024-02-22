"""
Hunter McMahon
Cis 210
Sources: Based off of example in textbook: "Python Programming in Context" by Bradley Miller et. al.
Description: I am Arthur, King of the britons and I seek the pi - Monty 'Pi'-then
"""
# import important stuff
import doctest
import math
import random


def pi_mc(num_darts: int) -> float:
    """
    Approx pi based on number of "darts" land in a circle with = radius of square plane
    theory states the the ratio of darts inside vs. outside the circle is pi
    Args:
        num_darts: (int) number of dart we 'throw' at the board

    Returns:
        an approx of pi

    >>> round(pi_mc(1_000_000), 2)
    3.14
    >>> round(pi_mc(10_000_000), 2)
    3.15
    >>> round(pi_mc(25_000_000), 2)
    3.15

    """
    hits = 0
    for i in range(num_darts):
        dart_x = random.random()
        dart_y = random.random()

        hype = math.sqrt(dart_x**2+dart_y**2)

        if hype <= 1:
            hits += 1

    pi = hits / num_darts * 4
    return pi


print(doctest.testmod())
