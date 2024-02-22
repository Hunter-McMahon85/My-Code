# CIS 122 Fall 2020 Assignment 1
# Author: Hunter McMahon
# Credit: Worked alone
# Description: Introduction to programming problem set
# uses Python numeric data types and operations to solve a variety
# of small problems.


import math

#
# Question 1
#
print("Question 1")
print("------------------------------------------")
# Calculate the number of watermelons given 120 children at 3 slices
# 130 adults at 2 slices, 15 slices per watermelon, add 20% extra,
# rounding up.

# Initialize variables with values
# ** your code **
children = 50
slices_per_child = 3
adults = 25
slices_per_adult = 2
slices_per_watermelon = 11
extra = 0.2
# Calculate the total number of watermelon slices and display the number of slices
total_slice = children*slices_per_child+adults*slices_per_adult
print('Total slices:', total_slice)

# Add extra amount and display number of slices
def total_extra():
    per_extra = total_slice*extra
    extra_tote = per_extra+total_slice
    return extra_tote
print('Total slices (including extra):', total_extra())

# Calculate the number of watermelons and display the number of watermelons
total_melons = total_extra()/slices_per_watermelon
print('Total watermelons:', total_melons)

# Rounds the number of watermelons up and display the number of watermelons
round_melon = math.ceil(total_melons)
print('Total watermelons (rounded up):', round_melon)

#
# Question 2
#
print()
print("Question 2")
print("------------------------------------------")
# Calculate the total number of trips given 100, 500, 1000, or 5000 daily steps,
# 16 steps per floor, and down and back up the stairs as one trip.
# Reuse the step variable. Round the number of trips up to the nearest
# whole integer.
# Recommended variable names: steps_per_floor, target_steps, trips

# Initialize variables
steps_per_floor = 31
target_steps = 100, 500, 1000, 5000
floors = 13
def trips(steps):
    trip = floors*2*steps_per_floor
    trips_raw = steps/trip
    trips_rounded= math.ceil(trips_raw)
    print ('Trips for', steps, 'steps:', trips_rounded)


# Calculate 100 steps and display the number of trips
trips(target_steps[0])

# Calculate 500 steps and display the number of trips
trips(target_steps[1])

# Calculate 1000 steps and display the number of trips
trips(target_steps[2])

# Calculate 5000 steps and display the number of trips
trips(target_steps[3])

#
#Question 3
#
print()
print("Question 3")
print("------------------------------------------")
# Calculate total distance walked per week given a pivot radius of 90 feet,
#five pivots, two inspections per day, and working five days a week. Round
#all results to two decimal places. Use 3.14, or math.pi, for the
# circumference equation calculation.

#Initialize variables
pie = math.pi
radius = 15
num_pivots = 7
inspects_per_day = 3
workdays = 7
# Calculate the circumference of one pivot
pivot = 2*pie*radius

# Calculate and display total distance walked (feet and miles)
def weekly_distance():
    perday = pivot*num_pivots*inspects_per_day
    perweekft = perday*workdays
    perweekmi = perweekft/5280
    print("Weekly distance (feet):", round(perweekft,2))
    print("Weekly distance (miles):", round(perweekmi,2))
weekly_distance()

