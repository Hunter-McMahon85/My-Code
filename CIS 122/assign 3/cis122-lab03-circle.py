# CIS 122 spring 2021 Lab 3
# Author: Hunter McMahon
# Partner: completed solo during lab with GE luis
# Description: the wheels on the bus go round and round... we're drawing circles...

#Import Turtle graphics module and create a turtle for drawing
import turtle
t = turtle.Turtle()

#Draws three concentric circles with the circle(radius) operator 

def move(t, x, y):
    """    Move Turtle to x, y position    """
    t.pu()
    t.goto(x, y)
    t.pd()
    
def draw_circle(t, radius, x, y):
    move(t,x,y-radius)
    t.circle(radius)
    

#draw_circle(t, 100, -100, -100) 
"""start_size = 50
for i in range(3):
    draw_circle(t, start_size, 0, 0)
    start_size = start_size + 25"""

def draw_concentric_circles(n, radius, gap, x, y):
    for i in range(n):
        draw_circle(t, radius, x, y)
        radius = radius + gap

#test
draw_concentric_circles(3, 50, 25, 0, 0) 
