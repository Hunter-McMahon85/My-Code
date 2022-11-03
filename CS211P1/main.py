"""
Hunter McMahon
CIS 211
Project 1 - main
this appears to be the main control center of this operation
"""
import planet
import sun
import solarsystem


def main():
    """
    main function to create an example solar system
    :return: (void)
    """
    our_star = sun.Sun("Blue Dwarf", 69000, 4200000, 2560)
    # these are planets from halo lore
    reach = planet.Planet("Reach", 15273, 60000502235022.05, 50000)
    harvest = planet.Planet("Harvest", 4012, 815156416516501, 60000)
    erebus = planet.Planet("Erebus VII", 3073, 546435468135.023354, 70000)
    meridian = planet.Planet("Meridian", 3507, 354681854234245.354643, 80000)
    fan_fic_ss = solarsystem.SolarSystem(our_star)
    fan_fic_ss.add_planet(reach)
    fan_fic_ss.add_planet(harvest)
    fan_fic_ss.add_planet(erebus)
    fan_fic_ss.add_planet(meridian)
    fan_fic_ss.show_planets('distance')



if __name__ == "__main__":
    main()
