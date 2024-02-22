"""
Hunter McMahon
CIS 211
Project 1 - sun
as the twin suns of tatooine set....
"""


# Place your Sun class definition here
class Sun:
    def __init__(self, name: str, radius: float, mass: float, temperature: float):
        """
        initiator for an instance of the sun class
        :param name: (str) name of the sun
        :param radius: (float) radius of the sun
        :param mass: (float) mass of the sun
        :param temperature: (float) temperature of the sun
        """
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temperature = temperature

    def get_name(self) -> str:
        """
        gets the name of the sun class instance
        :return:
        self.__name: (str) the string that is the sun name
        """
        return self.__name

    def get_radius(self) -> float:
        """
        gets the radius value for the sun class instance
        :return:
        self.__radius: (float) the radius value for the sun
        """
        return self.__radius

    def get_mass(self) -> float:
        """
        gets the mass value for the sun class instance
        :return:
        self.__mass: (float) the mass value for the sun
        """
        return self.__mass

    def get_temperature(self) -> float:
        """
        gets the temperature value for the sun class instance
        :return:
        self.__mass: (float) the temperature value for the sun
        """
        return self.__temperature

    def __str__(self):
        """
        displays the data values for the sun
        :return: (void)
        """
        return f" Sun name:{self.__name} \n Sun Radius: {self.__radius} \n Sun Mass: {self.__mass} \n Sun Temperature: {self.__temperature}"
