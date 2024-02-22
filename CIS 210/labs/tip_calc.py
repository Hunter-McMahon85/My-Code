"""
Hunter McMahon
Cis 210
Desc: tip calc

"""
import doctest


def calc_tip(amount: float, sat_level: float) -> float:
    """
    calculates the tip to be added onto the bill
    Args:
        amount: total of the bill
        sat_level: customer satisfaction level

    Returns:
        tip_amount: (float) the amount of tip for the bill
    >>> print(calc_tip(20.5, 0))
    0.0
    >>> calc_tip(20.5, 1)
    2.0500000000000003
    >>> calc_tip(20.5, 2)
    4.1000000000000005
    """
    int(sat_level)
    tip = 0
    if sat_level == 0:
        tip = 0
    elif sat_level == 1:
        tip = .1
    elif sat_level == 2:
        tip = .2
    tip_amount = amount * tip
    return tip_amount


def main():
    """
    handles the tip calculation
    Returns:
        none
    """
    bill = input('Enter your bill amount: ')
    satis = input('How satisfied are you[0-2]? ')
    bill = float(bill)
    satis = float(satis)
    tip = calc_tip(bill, satis)
    total_with_tip = tip + bill
    print('Your tip is:', tip)
    print('The total is:', total_with_tip)


print(doctest.testmod())
