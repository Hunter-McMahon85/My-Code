# CIS 122 spring 2021 Lab 5
# Author: Hunter McMahon
# Partner: completed solo during lab with GE luis
# Description: lets multiply a bunch of numbers in decending order or something... haha big numbers go brrrr
import math

def factorial(num):
    """
    takes an integer input and calculates its factorial
        calculates the factorial for integers >= 0
    Args
    num: (int): number that we want to calculate the facotial of
    Returns:
    output: the factorial of a positive non-zero integer
    1: factorial of 0
    none: the input was negative and thus unsupported
    """
    #ensure num is an integer
    num = int(num)
    
    #check for negative input or if the input is 0
    if num < 0:
        print("Input must be >= 0")
        return None
    elif num == 0:
        return 1
    #for positive values, calculate the factoral
    else:
        output = 1
        for i  in range(1, num +1 ):
             output = output*i
        return output

#compare our function to the built in math function

def test_factorial(range_num, show = False):
    """
    test our factorial function by comparing it to the math.factorial method
    Args
    range_num: (int): number that we want to compare the factorials of
    show (boolean)(optional): decides whether or not to show the results for each value
    Returns:
    none, the function is void
    """
    errors = 0
    #intialize the testing loop
    for i in range(range_num +1):
        #compute our factorials
        my_result = factorial(i)
        math_result = math.factorial(i)

        #optional paramater to show both results
        if show == True:
            print(str(i)+":",  my_result, math_result)
            
        #compare the factorials to see if they match, if not we print out the number of errors
        if my_result != math_result:
            print(i)
            errors += 1
    print('Errors (' + str(range_num) + '): ', str(errors))

number = input("Enter factorial number:")
result = factorial(number)
print(result)
