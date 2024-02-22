"""
Hunter McMahon
Cis 210
Sources:
Description: so the gang is back together now ey
"""
# import our other functions
import doctest
import math
import p1arch
import p2wallis
import p3mc


def pi_allpi(err_tol: float):
    """
    gives values of what you can enter into the other methods of with given error tolerance
    Args:
        err_tol: (float) the error tolerance

    Returns:
        none

    >>> pi_allpi(.1)
    Archimedes: num_sides = 4
    Wallis: num_pairs = 2
    Monte Carlo: num_darts = 5

    >>> pi_allpi(.01)
    Archimedes: num_sides = 13
    Wallis: num_pairs = 25
    Monte Carlo: num_darts = 7

    >>> pi_allpi(.001)
    Archimedes: num_sides = 41
    Wallis: num_pairs = 250
    Monte Carlo: num_darts = 6


    """
    pi = math.pi
    if 0 < err_tol <= 1:
        archimedes = 2
        wallis = 1
        monte_carlo = 5

        # Archimedes up first
        arch_margin = True
        while arch_margin == True:
            arch_est = p1arch.pi_arch(archimedes)
            arch_percent_error = 1 - arch_est / pi
            if arch_percent_error <= err_tol:
                arch_margin = False
            else:
                archimedes += 1

        # then wallis
        wall_margin = True
        while wall_margin == True:
            wall_est = p2wallis.pi_wallis(wallis)
            wallis_percent_error = 1 - wall_est / pi
            if wallis_percent_error <= err_tol:
                wall_margin = False
            else:
                wallis += 1
        # then monte

        monte_margin = True
        while monte_margin == True:
            monte_est = p3mc.pi_mc(monte_carlo)
            monte_percent_error = 1 - monte_est / pi
            if monte_percent_error <= err_tol:
                monte_margin = False
            else:
                monte_carlo += 1

        # now to display
        print('Archimedes: num_sides =', archimedes)
        print('Wallis: num_pairs =', wallis)
        print('Monte Carlo: num_darts =', monte_carlo)
    else:
        print('ValueError: err_tol should be a floating - point number in (0, 1]')


print(doctest.testmod())
