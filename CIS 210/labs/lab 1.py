'''
CIS 210 Lab 1–Lab 1 Exercises
Author: Hunter McMahon
Credits: nopartners nor outside resource consulted
Lab exercisesdemonstrating how IDLE Editor and Shell interact.
'''

welcome = 'hello, python'

def is_even(n):
    '''(int) -> BooleanReturns True if n is an even number.
    >>>is_even(100)True
    >>>is_even(101)False
    >>>is_even(0)True'''
    return (n % 2) == 0
