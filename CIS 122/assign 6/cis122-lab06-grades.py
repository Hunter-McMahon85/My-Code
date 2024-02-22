# CIS 122 spring 2021 Lab 6
# Author: Hunter McMahon
# Partner: completed solo during lab with GE luis
# Description: lets see how you did on the test here eh

#initialize variables
count = 0
average = 0
#this is so that the lowest score gets updated off the start
lowest = 100
highest = 0
totalscore = 0
taking_input = True
#use a while loop
while taking_input == True:
    #ask for input and add it to a variable
    newscore = input('Enter score: ')
    #check if input is blank
    if len(newscore) == 0:
        #if so end the loop and print the results
        print('Count: ', count, '\nAverage: ', average, '\nLow score: ', lowest, '\nHigh score: ', highest)
        taking_input = False
        break
    # if not, update variables, and reiterate the loop
    elif len(newscore) != 0:
        scorenum = int(newscore)
        count +=1
        totalscore += scorenum
        average = totalscore/count
        if scorenum > highest:
            highest = scorenum
        elif scorenum < lowest:
            lowest = scorenum
