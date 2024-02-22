'''
Project 1 part 3
CIS 210
Hunter McMahon
(and yes the second M in my last name is meant to be capitalized)
Sorces: I took 122 however not all aspects of the turtle were covered so
I refered to the python documentation as a refresher and to learn some comands
that werent taught
https://docs.python.org/3/library/turtle.html
Description: QUACK!
'''

#import and assign our turtle to a variable
import turtle
t = turtle

#function to handle drawing
def draw_a_duck():
    '''
    Type: Void
    Purpose: draws a mallard outline when called
    Example of use: draws an instant friend for a lonley person
    '''
    t.pu()
    t.goto(-250,50)
    t.pd()
    t.fd(50)
    #back
    t.lt(10)
    t.fd(50)
    t.lt(5)
    t.fd(50)
    t.lt(2.5)
    t.fd(50)
    t.rt(17.5)
    t.fd(75)
    t.rt(2.5)
    t.fd(50)
    t.rt(5)
    t.fd(25)
    #back of kneck
    t.lt(7.5)
    t.lt(80)
    t.fd(150)
    #head
    t.rt(55)
    t.fd(25)
    t.rt(25)
    t.fd(50)
    t.rt(45)
    t.fd(60)
    t.lt(15)
    t.fd(75)
    t.lt(45)
    #neck and chest
    t.bk(75)
    t.rt(15)
    t.bk(45)
    t.lt(80)
    t.bk(70)
    t.rt(140)
    t.fd(50)
    t.rt(30)
    t.fd(50)
    t.rt(20)
    t.fd(50)
    t.rt(10)
    t.fd(20)
    t.rt(10)
    t.fd(20)
    t.rt(50)
    #belly and feet
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(50)
    t.bk(75)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(50)
    #finish its tail
    t.goto(-250,50)
    t.fd(15)
    
#draw the Duck
draw_a_duck()
