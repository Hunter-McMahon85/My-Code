"""
Hunter McMahon
CIS 211
Test planet class project 1
test and debug time
"""
# TODO: write your planet.Planet unit tests

import unittest
from planet import Planet

"""
class name(unittest.TestCase):
    def test_name(self):
        object_variable = example of object
        self.assertEqual(object_variable.object_method(), expected output)
"""


class Test_Get_Name(unittest.TestCase):
    def test_name(self):
        """
        test the get_name function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 1, 1, 1)
        self.assertEqual(plan_ob.get_name(), "reach")

    def test_name_empty(self):
        """
        test the get_name function of the planet class
        :return: (void)
        """
        plan_ob = Planet("", 1, 1, 1)
        self.assertEqual(plan_ob.get_name(), "")


class Test_Radius(unittest.TestCase):
    def test_name(self):
        """
        test the get_radius function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 2001, 1, 1)
        self.assertEqual(plan_ob.get_radius(), 2001)


class Test_Mass(unittest.TestCase):
    def test_name(self):
        """
        test the get_mass function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 1, 7000, 1)
        self.assertEqual(plan_ob.get_mass(), 7000)


class test_distance(unittest.TestCase):
    def test_name(self):
        """
        test the get_distance function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 1, 1, 85)
        self.assertEqual(plan_ob.get_distance(), 85)


class test_volume(unittest.TestCase):
    def test_name(self):
        """
        test the get_volume function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 4, 1, 1)
        self.assertEqual(round(plan_ob.get_volume(), 2), 268.08)


class test_sa(unittest.TestCase):
    def test_name(self):
        """
        test the get_surface_area function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 4, 1, 1)
        self.assertEqual(round(plan_ob.get_surface_area(), 2), 201.06)


class test_density(unittest.TestCase):
    def test_name(self):
        """
        test the get_density function of the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 4, 20, 1)
        self.assertEqual(round(plan_ob.get_density(), 4), 0.0746)


class test_set_name(unittest.TestCase):
    def test_name(self):
        """
        test the set name function for the planet class
        :return: (void)
        """
        plan_ob = Planet("reach", 1, 1, 1)
        plan_ob.set_name("harvest")
        self.assertEqual(plan_ob.get_name(), "harvest")


if __name__ == '__main__':
    unittest.main()
