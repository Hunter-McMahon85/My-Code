'''
Project 1 part 2
CIS 210
Hunter McMahon
(and yes the second M in my last name is meant to be capitalized)
Sorces:
https://www.andrew.cmu.edu/user/gkesden/ucsd/classes/wi17/cse160-a/applications/ln/lecture17.pdf
https://docs.python.org/3/tutorial/floatingpoint.html
Description: I created some chaos by creating some examples of real number and floating point properties causing errors
'''

#our good integers
a = 15
b = 35
c = 1

#foating  point troublemakers
v = .000005
w = -.000005
x = .000015
y = .1
z = .4

#now for out naughty numbers to cause some chaos 

#example 1, Cumulative/Associative property of addition
print((c+v)+z==c+(v+w))

#example 2,Cumulative/Associative property of multiplication
print((c*v)*z==c*(v*w))

#example 3, Multiplicative inverse property
print(v*(1/w) == 1)

#the 1st 3 i found after seeing https://www.andrew.cmu.edu/user/gkesden/ucsd/classes/wi17/cse160-a/applications/ln/lecture17.pdf

#example 4, some basic additon doesnt work with long enough variables found: https://docs.python.org/3/tutorial/floatingpoint.html
print(v+v+v==x)

#example 5, I could not, For the life of me, think of a 5th example
print()
