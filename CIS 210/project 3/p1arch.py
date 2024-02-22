"""
Hunter McMahon
Project 3 part 1: archimedes method
Source: Based of off example in textbook: "Python Programming in Context" by Bradley Miller et. al.
Description: What exactly is pi, lets have archimedes take a guess
"""
# import required modules
import doctest
import math


# function for Archimedes method


def pi_arch(num_sides: int) -> float:
    """
    function which conducts archimedes method of estimating pi
    Args:
        num_sides: (Int) number of sides to be used in the shape that will approx. pi

    Returns:
        an approx of pi
    >>> pi_arch(200)
    3.141463462364135
    >>> pi_arch(3000)
    3.1415920793995156
    >>> pi_arch(3)
    2.598076211353316


    """
    in_angle_b = 360.0 / num_sides
    half_angle_a = in_angle_b / 2
    side_s = math.sin(math.radians(half_angle_a)) * 2
    # full_side_s = half_side_s*2
    poly_circumference = num_sides * side_s
    pi = poly_circumference / 2
    return pi


print(doctest.testmod())
