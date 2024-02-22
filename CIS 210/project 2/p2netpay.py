'''
Hunter McMahon
Project 2 pt 2. Net-Pay
CIS 210
Sources: None (prior cis 122 knowledge)
Tax fraud is bad kids, and dont think the IRS wont catch you... They will... nobody escapes the IRS...
'''

#our tax
def tax(gross_pay):
    '''
    Calculates the amount of tax taken out of ones gross pay by multipling it by the tax rate
    Paramaters:
    gross_pay (float/int): ones pay before tax
    returns the amount of money taken out by tax as a float/int value
    '''
    return gross_pay * .15

#finding the net pay
def netpay(hours_worked):
    '''
    takes the parameter of hours worked and determines the gross pay based
    on the $16.25 wage and then subtracts the tax from it before rounding it
    to 2 decimal places
    Parameters:
    hours_worked (float/int): the number of hours one worked in a week
    Returns:
    (Float/int) the net pay of the worker after tax
    '''
    pay_by_hour = 16.25
    gross_pay = pay_by_hour * hours_worked
    return round(gross_pay - tax(gross_pay), 2)

#main function is to display test.py cases
def main():
    '''Net pay program driver.'''
    print('For 1 hour of work, netpay is: ', netpay(1)) 
    print('For 40 hours of work, netpay is: ', netpay(40))
    return None 

main()
