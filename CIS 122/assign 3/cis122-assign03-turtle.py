# CIS 122 spring 2021 reverse
# Author: Hunter McMahon
# Partner: completed solo 
# Description: the turtle will now draw on the sand, time for some jammin beach tunes

import turtle
t = turtle
#part A
def draw_line(t, x, y, angle, length):
    """
    draws a line
        draws a line based on x,y,angle & length, pen is up at the end
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    t (Turtle): Drawing Turtle
    x (int/float): starting x coordinate
    y (int/float): starting y coordinate
    angle(int/float): angle of the line
    lenght(int/float): length of the line
    Returns:None
    """
    t.pu()
    t.setx(x)
    t.sety(y)
    t.seth(angle)
    t.pd()
    t.fd(length)
    t.pu()
    
#test cases
#draw_line(t, 100, 100, 0, 200)
#draw_line(t, -100, -100, 270, 50)
#draw_line(t, 200, 200, 45, 75)

#part E
def draw_radial_lines(t, x, y, length, num_lines):
    """
    draws a series of lines
        draws a series of radial lines based on x, y coordinates & length, pen is up at the end
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    t (Turtle): Drawing Turtle
    x (int/float): starting x coordinate/center of radial lines
    y (int/float): starting y coordinate/center of radial lines
    lenght(int/float): length of the radial lines
    num_lines(int): number of radial lines
    Returns:None
    """
    lines = int(num_lines)
    angles = 360/lines
    for i in range(lines):
        draw_line(t, x, y, angles*i+1, length)
#test cases
#draw_radial_lines(t, -100, -100, 25, 8)
#draw_radial_lines(t, -100, 100, 100, 4)
#draw_radial_lines(t, 100, -100, 200, 16)
#draw_radial_lines(t, 100, 100, 50, 32)

#part e
def draw_radials_in_quadrants(t, length, num_lines):
    """
    draws a series of radial lines
        draws a series of radial lines (with a number of lines, 1 in each quadrant of the graph based on length
    Args:    <Each parameter, followed by type, colon, and a description of the paramter>
    t (Turtle): Drawing Turtle
    lenght(int/float): length of the radial lines, also determins space between the lines
    num_lines(int): number of radial lines
    Returns:None
    """
    space = length*2
    draw_radial_lines(t, space , space, length, num_lines)
    draw_radial_lines(t, -space , space, length, num_lines)
    draw_radial_lines(t, -space , -space, length, num_lines)
    draw_radial_lines(t, space , -space, length, num_lines)

#test cases
#draw_radials_in_quadrants(t, 75, 8)
#draw_radials_in_quadrants(t, 50, 16)

#submission case

draw_radials_in_quadrants(t, 100, 12)
    
