"""
Hunter McMahon
Cis 210
Sources:
Description: so many dots...
"""

import math
import turtle
import random


def mc_vis(num_darts: int):
    """

    Args:
        num_darts:

    Returns:

    """
    # make a background grid
    turtle.speed('fastest')
    turtle.pd()
    turtle.forward(200)
    turtle.back(400)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.back(400)
    turtle.forward(200)
    turtle.pu()
    turtle.goto(100, 0)
    turtle.pd()
    turtle.circle(100, 360)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.pu()

    # add the points
    for i in range(num_darts):
        polarity_x = random.random()
        polarity_y = random.random()
        dart_x = 0
        dart_y = 0
        # determine our points on a 4 grid plane
        # x
        if polarity_x <= .49:
            dart_x = -random.random()
        if polarity_x >= .5:
            dart_x = random.random()
        # y
        if polarity_y <= .49:
            dart_y = -random.random()
        if polarity_y >= .5:
            dart_y = random.random()

        # will be used to determine if point is in the circle
        hype = math.sqrt(dart_x ** 2 + dart_y ** 2)

        # time to visualize
        turtle.speed('fastest')

        if hype <= 1:
            turtle.pu()
            turtle.goto(dart_x*100, dart_y*100)
            turtle.pd()
            turtle.dot(5, 'green')
            turtle.pu()

        elif hype > 1:
            turtle.pu()
            turtle.goto(dart_x*100, dart_y*100)
            turtle.pd()
            turtle.dot(5, 'red')
            turtle.pu()


mc_vis(1000)
