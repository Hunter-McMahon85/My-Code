# CIS 122 spring 2021 Lab 2
# Author: Hunter McMahon
# Partner: Completed during lab 2 with GE Luis
# Description: Create a function that returns the square of any positive integer

# Define a function that accepts a number
def square(num):
    # Verify that the input is a positive integer (methood to do so hasnt been taught)
    # Multiply the number by itself
    result = num*num
    # Return the solution to the math problem
    return result
# print the sample
two = str(square(2))
ten = str(square(10))
hundred = str(square(100))
print (two+",", ten+",", square(100))
# Test and debug if needed
