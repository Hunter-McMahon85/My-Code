"""
Hunter McMahon
CIS 211
Mini Project 1
awww its a cute little itsy bitsy miny project... so cute... not as cute as puppies though...
"""
# Note about using Point as a type in type hints.
# Because Point is a user-defined class, it is not recognized 
# as a type in type hints until we do the following:
from typing import TypeVar

Point = TypeVar("Point")


# TODO: place your implementation of the Point class here
class Point:
    def __init__(self, x: int, y: int):
        """
        Initializes the x and y coordinates in the point object instance
        :param x: (int) starting x coordinate
        :param y: (int) starting y coordinate
        """
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        """
        moves the coordinates by adding a specified value to them
        :param dx: (int) x value being added
        :param dy: (int) y value being added
        :return:
        none, we only modify existing variables
        """
        self.x += dx
        self.y += dy

    def __eq__(self, other) -> bool:
        """
        checks to see if the coordinate in this class object equals that of another instance of the class object
        :param other: another instance of the class object
        :return:
            (boolean) True or false depending on whether or not the instances are equal
        """
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __str__(self) -> str:
        """
        returns the class object as an string
        :return:
            (str) the coordinate as a string (in interval notation
        """
        return f"({self.x}, {self.y})"
