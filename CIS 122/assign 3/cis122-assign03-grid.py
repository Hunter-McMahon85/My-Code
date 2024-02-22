# CIS 122 spring 2021 grid
# Author: Hunter McMahon
# Partner: completed solo 
# Description: Attention to the designated grid square!!!!!

#the grid function
def draw_grid(n):
    """
    prints a small grid of numbers
    prints a grid of n numbers n times theres not much else to it, why does this even need a detailed description?
    Args:
    n(integer)
    description of n Returns:
    none (void)
    """ 
    numout = ""
    for i in range(n):
        #if statements ensure theres no spaces to the left of on or to the right of the final value
        if i >= 0:
            numout = numout + str(i+1) + " " 
        if i == n:
            numout = numout + str(i+1)
    for i in range(n):
        print(numout)

#test case

#draw_grid(4)

#submission case

draw_grid(5)
