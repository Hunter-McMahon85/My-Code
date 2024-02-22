# File: is_even.py
'''
def is_even(n: int) -> bool: 
    """ Determines if n is an even number.

    Args:
        n: an integer number

    Returns:
        True if n is an even number, False otherwise

    >>> is_even(100)
    True
    >>> is_even(101)
    False
    >>> is_even(0)
    True
    """
    print('in function is_even')

    return (n % 2) == 0
is_even(2)
result = print(is_even(3))

def welcome():
   """Print a welcome message. 
   >>> welcome()
   Good morning, CIS 210!
   """
   print('Good morning, CIS 210!')
   return None
 
welcome()
'''
#excersize 2
# File: est_tax.py

def est_tax(income: float, exemptions: float) -> float:
    """Generates an estimate for federal income tax and print the result.
    Calls the function taxable to compute the     
    Assumes a simple standard deduction of $6500 and a flat tax rate of 20%.
    (Example from class, revised to print (not return) estimated tax.)
  
    Args:
        income: gross income, for which the tax is being computed
        exemptions: the number of exemptions claimed by the tax payer

    Returns:
        The tax owed for the provided income and number of exemptions.

    >>> est_tax(43000, 1)
    3580.0
    """

    # Constants for the standard exemption and deduction (USD)
    STD_DEDUCT = 12550
    STD_EXEMPT = 12550

    # Constant for the flat tax rate of 20%
    TAX_RATE = .20

    # Calculate federal tax by adjusting reported income and applying tax rate
    taxable_income = taxable(income, exemptions, STD_EXEMPT, STD_DEDUCT)
    estimated_tax = taxable_income * TAX_RATE

    print('Estimated tax is:', estimated_tax)

    return estimated_tax

def taxable(income: float, exemptions: int, exempt_amount: float, deduct_amount: float): 
    """Adjust gross income to taxable income by applying the 
       standard deduction and exemptions.
  
    Args:
        income: gross income, for which the tax is being computed
        exemptions: the number of personal exemptions
        exempt_amount: the dollar amount for each exemption
        deduct_amount: the dollar amount for the standard deduction

    Returns:
        TODO: Should this function return a value or print the result??
        taxable_income(float):
        total of all taxbable income
       
    >>> taxable(43000, 1, 12550, 12550)
    17900
    """

    # TODO: Write the function code here, pay special attention to the return
    taxable_income = income-(exemptions*exempt_amount+deduct_amount)
    return taxable_income
print(taxable(43000, 1, 12550, 12550))
