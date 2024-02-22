# CIS 122 spring 2021 lab 8 word stats
# Author: Hunter McMahon
# Partner: completed solo during lab session
# Description: listing some stuff... 

import random
def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    #generates a list of random numbers based on a given range and amount with default values
    t = []
    if num <= 0:
        print('num must be > 0')
    elif not isinstance(num, int):
        print('num must be an integer')
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
        print('start_range and end_range must be integers')
    else:
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)
        if sort_list.upper() == 'Y':
            t.sort()
    return t

#get a list of 100 random int   
t = gen_random_integer_list(100)

#find the high score
def get_high_score(t):
    highscore = 0
    if isinstance(t, list) == True:
        tcopy = t[::]
        tcopy.sort()
        if len(t) > 0:
            highscore = tcopy[len(t)-1]
    else:
        print('List argument expected')
        highscore = -1
    return highscore

#find the low score
def get_low_score(t):
    lowscore = 0
    if isinstance(t, list) == True:
        tcopy = t[::]
        tcopy.sort()
        if len(t) > 0:
            highscore = tcopy[0]
    else:
        print('List argument expected')
        highscore = -1
    return highscore

#get the average
def get_mean_score(t):
    mean = 0
    total = sum(t)
    if isinstance(t, list) == True:
        if len(t) > 0:
            mean = total/len(t)
    else:
        print('List argument expected')
        highscore = -1
    return mean

#find the median score
def get_median_score(t):
    median = 0
    if isinstance(t, list) == True:
        if len(t) > 0:
            tcopy = t[::]
            tcopy.sort()
            #for when list has odd num of values
            if len(t) % 2 == 1:
                index = len(t) // 2
                median = tcopy[index]
            #when the list has an even num of values
            else:
                index1 = len(t) // 2
                index2 = index1 - 1
                median = (tcopy[index1] + tcopy[index2])//2              
    else:
        print('List argument expected')
        median = -1
    return median

#find the ranges or something
def count_range(t, start, end):
    if isinstance(t, list) == True:
        if len(t) == 0:
            return 0
        else:
            if isinstance(start, int) == False or isinstance(end, int) == False:
                print('start and end must be integers')
                return -1
            elif start > end or start == end:
                print('start must be < end')
                return -1
            else:
                count = 0
                for number in t:
                    if start <= number <= end:
                        count += 1
                return count
    else:
        print('List argument expected')
        return -1
def list_range(t):
    print('A -',count_range(t, 90, 100))
    print('B -',count_range(t, 80, 89))
    print('C -',count_range(t, 70, 79))
    print('D -',count_range(t, 60, 69))
    print('F -',count_range(t, 0, 59))








