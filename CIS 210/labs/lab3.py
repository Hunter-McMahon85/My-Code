# Pizza calculator example code
import doctest
import math

def circle_area(diameter):
    """ calcs circle area
        param:
        diameter: float/int
        return:
        area of cirlce
    """
    radius = diameter/2
    return math.pi*radius**2

def pizza_calculator(diameter, cost): 
    ''' 
    (int, num) -> float 

    Calculates and returns the cost per square inch 
    of pizza for a pizza of given diameter and cost. 
    Examples: 

    >>> pizza_calculator(14, 18) 
    0.117 
    >>> pizza_calculator(14, 20.25)  
    0.132 
    '''
    
    area = circle_area(diameter)

    cost_per_inch = cost / area 
    cost_per_inch = round(cost_per_inch, 3) 
    return cost_per_inch

def is_even(n): 
    ''' (int) -> boolean
    
    Returns True if n is even, False otherwise. 
    
    >>> is_even(8) 
    True 
    >>> is_even(5) 
    False 
    ''' 
    return n % 2 == 0
    
def perror(msg, line): 
    ''' (string, int) -> None
    
    Prints "Error: " followed by formatted line number and message. 
    Returns None.
    
    >>> perror("input too large", 27) 
    Error: (line 27) input too large 
    ''' 

    print( "Error: (line ", line,  ") ",  msg) 
    return None

print(doctest.testmod())

