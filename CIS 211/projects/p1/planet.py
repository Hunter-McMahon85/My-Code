"""
Hunter McMahon
CIS 211
Project 1 - planet
it appears that the title scroll has finished and now we see in view a planet...
"""
import math


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float):
        """
        initiator function for a new instance of the planet class
        :param name: (str) the planet name
        :param radius:  (float) the planet radius
        :param mass: (float) the planet mass
        :param distance: (float) distance from the center/sun (i think textbook instructions dont clarify this)
        """
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance

    # 10.3.2 Accessor Methods
    def get_name(self) -> str:
        """
        gets the name of the planet class instance
        :return:
        self.__name: (str) the string that is the planets name
        """
        return self.__name

    def get_radius(self) -> float:
        """
        gets the radius value for the planet class instance
        :return:
        self.__radius: (float) the radius value for the planet
        """
        return self.__radius

    def get_mass(self) -> float:
        """
        gets the mass value for the planet class instance
        :return:
        self.__mass: (float) the mass value for the planet
        """
        return self.__mass

    def get_distance(self) -> float:
        """
        gets the distance value for the planet class instance
        :return:
        self.__mass: (float) the mass value for the planet
        """
        return self.__distance

    def get_volume(self):
        """
        calculates the volume for the planet for the class instance
        :return: (float) the planets volume
        """
        return (4/3) * math.pi * self.__radius ** 3

    def get_surface_area(self):
        """
        calculates the surface area for the class instance
        :return: (float) the planets surface area
        """
        return 4 * math.pi * self.__radius ** 2

    def get_density(self):
        """
        calculates the density of the planet for the class instance
        :return: (float) the planets density value
        """
        return self.__mass / self.get_volume()

    def set_name(self, new_name: str):
        """
        renames the planet in the class instance
        :param new_name: (str) the new name for the planet
        :return: void
        """
        self.__name = new_name

    def __str__(self) -> str:
        """
        returns the name of the planet as a string for the class object instance
        :return:
            (str) the planet name as a string
        """
        return f"{self.__name}"
