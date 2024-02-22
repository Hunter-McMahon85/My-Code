'''
    CIS 122 spring 2021 assignment 2 cement
    Author: Hunter McMahon
    Partner: Completed solo
    Description: calculate how much cement do my imaginary friends need
'''
#import math object
import math

#Return cement amount in yards using cubic inches given thickness (t),
#width (w), and length (l) , in inches.

def cubic_yards_cement(t, w, l):
    #establish size of a cubic yard in inches
    cubic_yard = math.pow(36, 3)
    #find volume of slab
    slab_volume = w*t*l
    #retun rounded value of cubic yards in the slab
    return round(slab_volume/cubic_yard, 2)

#Output (print) results of calculating yards given
#thickness (t), width (w),  and length (l)  in inches

def print_results(t, w, l):
    print ('A cement slab', str(t)+'"', 'thick,', str(w)+ '"', 'wide, and', str(l)+'"', 'long requires', cubic_yards_cement(t, w, l), 'cubic yards of cement')

#test
#print_results(4,48,144)
#print_results(4,180,240)
    
#submission output
print_results(3,15,100)

'''
refrences
https://www.concretenetwork.com/concrete/howmuch/calculator.htm
https://todayshomeowner.com/cubic-yard-calculator/
