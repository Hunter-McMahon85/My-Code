'''
    CIS 122 spring 2021 assignment 2 travel
    Author: Hunter McMahon
    Partner: Completed solo
    Description: how long will it take to travel? lets find out
'''
#import math object
import math 
# Calculate travel time in minutes given the distance in miles and the speed in mph
def calc_travel_time(distance, speed):
    #find time in hours (dis/mph)
    time_hour = distance/speed
    #convert to min (*60)
    time_min = time_hour*60
    return time_min

#Output the travel time hours, minutes,  seconds, given distance, and speed
def print_travel_time(distance, speed):
    #calculate time values 
    hours = math.floor(distance/speed)
    minutes = calc_travel_time(distance, speed)-(hours*60)
    seconds = (minutes-math.floor(minutes))*60
    #output final message
    print('To travel', distance, 'miles at', speed,'MPH will take', int(hours), 'hr,', int(minutes), 'min, and', int(seconds), 'sec')

#test cases
'''
print_travel_time(120, 55)
print_travel_time(120, 70)
print_travel_time(5, 25)
print_travel_time(5, 35)
'''
#submission case
#   Output the travel time hours, minutes, seconds, given distance, and speed
print_travel_time(26.2, 13.16)

'''
references

https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php

'''
