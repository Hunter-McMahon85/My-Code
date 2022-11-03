"""
Hunter McMahon
CIS 211
Project 1 - solar system
what surrounds the sun?
"""
# Place your SolarSystem class definition here


class SolarSystem:
    def __init__(self, star):
        """
        initiator function for an instance of the Solar system class
        :param star: an instance of the sun class from Sun.py that is the sun for our solar system
        """
        self.__thesun = star
        self.__planets = []

    def add_planet(self, new_planet):
        """
        adds a planet to the list of planets in the solar system
        :param new_planet: (obj) an instant of the planet object to be added to the planets list
        :return: (void)
        """
        self.__planets.append(new_planet)

    def show_planets(self, sortby: str = ''):
        """
        displays the planets in the solar system class instance
        :param sortby: (str) category to sort by
        :return: (void)
        """
        if sortby == '':
            for planet in self.__planets:
                print(planet)
        elif sortby == 'name':
            namelist = []
            for i in range(len(self.__planets)):
                namelist.append(self.__planets[i].get_name())
            namelist.sort()
            for i in namelist:
                print(i)
        elif sortby == 'distance':
            distlist = []
            for i in range(len(self.__planets)):
                distlist.append([self.__planets[i].get_distance(), self.__planets[i].get_name()])
            distlist.sort()
            for i in distlist:
                print(i[1])
        elif sortby == 'mass':
            masslist = []
            for i in range(len(self.__planets)):
                masslist.append([self.__planets[i].get_mass(), self.__planets[i].get_name()])
            masslist.sort()
            for i in masslist:
                print(i[1])
        elif sortby == 'radius':
            radlist = []
            for i in range(len(self.__planets)):
                radlist.append([self.__planets[i].get_radius(), self.__planets[i].get_name()])
            radlist.sort()
            for i in radlist:
                print(i[1])
