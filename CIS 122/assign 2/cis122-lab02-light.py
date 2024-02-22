# CIS 122 Fall 2020 Lab 2
# Author: Hunter McMahon
# Partner: completed solo during lab with GE luis
# Description: calculating the speed of light or time it takes to travel, something like that


#function to find average time for light to travel from the sun to an object at set distance (in miles).
def avg_light_travel_seconds(distance_miles):
    #divide the distance by the speed light travels at in MI per second
    raw = distance_miles/186282
    #round the output to 2 decimal points 
    desired = round(raw, 2)
    #return the output
    return desired

#displaying our results for pluto and earth
def print_results(planetary_object, avg_light_travel_seconds):
    print("Light travels from the sun to the", planetary_object, "an average of", avg_light_travel_seconds, "seconds.")


#output must be:
#Light travels from the sun to the Earth an average of xxx.xx seconds.
#Light travels from the sun to Pluto an average of yyy.yy seconds.
#output must include round() to 2 decimal places

#call the print function for earth and pluto
print_results("the Earth", avg_light_travel_seconds(93000000))
print_results("Pluto", avg_light_travel_seconds(3670050000))
