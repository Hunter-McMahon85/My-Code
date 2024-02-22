"""
Hunter McMahon
CIS 211
Test planet class project 1
test and debug time
"""

import unittest
from sun import Sun


class Test_Get_Name(unittest.TestCase):
    def test_name(self):
        """
        test the get_name function of the Sun class
        :return: (void)
        """
        sun_ob = Sun("Shiny", 1, 1, 1)
        self.assertEqual(sun_ob.get_name(), "Shiny")

    def test_name_empty(self):
        """
        test the get_name function of the Sun class
        :return: (void)
        """
        sun_ob = Sun("", 1, 1, 1)
        self.assertEqual(sun_ob.get_name(), "")


class Test_Radius(unittest.TestCase):
    def test_name(self):
        """
        test the get_name function of the Sun class
        :return: (void)
        """
        sun_ob = Sun("Shiny", 3035, 1, 1)
        self.assertEqual(sun_ob.get_radius(), 3035)


class Test_Mass(unittest.TestCase):
    def test_name(self):
        """
        test the get_mass function of the Sun class
        :return: (void)
        """
        sun_ob = Sun("Shiny", 1, 42096, 1)
        self.assertEqual(sun_ob.get_mass(), 42096)


class test_temperature(unittest.TestCase):
    def test_name(self):
        """
        test the get_temperature function of the Sun class
        :return: (void)
        """
        sun_ob = Sun("Shiny", 1, 1, 1000)
        self.assertEqual(sun_ob.get_temperature(), 1000)
