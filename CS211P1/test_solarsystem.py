"""
Hunter McMahon
CIS 211
Test planet class project 1
test and debug time, honestly because of how main was couldnt think of much to test here...
"""
# TODO: write your solarsystem.SolarSystem unit tests


import unittest
from solarsystem import SolarSystem
from sun import Sun
from planet import Planet



class TO_showing_Planets(unittest.testcase):
    def showin_off(self):
        """
        test the show planets method of the solar system class though it also test all aspects of it as well
        :return: (void)
        """
        starman = Sun("blue", 35, 45, 55)
        ss1 = SolarSystem(starman)
        p1 = Planet("Mandalore", 25, 55, 65)
        ss1.add_planet(p1)
        self.assertEqual(ss1.show_planets(), "Mandalore")
