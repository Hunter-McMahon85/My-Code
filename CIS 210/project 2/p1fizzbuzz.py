'''
Hunter McMahon
Project 2 pt 1. Fizzbuzz
CIS 210
Sources: 122 knowledge!
Do you want to play a game? no not buzzsaws, just fizzbuzz
'''
#set the doctest up for latter
import doctest

#lets make the game
def fb(n):
    '''
    N sets the range of numbers in the game and the user then inputs
    numbers within that range at which point the program test.py to see if
    its divisible by 3 (fizz) and/or 5 (buzz) and returns the words fizz or buzz accordingly
    Parameters:
    n (int or float): value that is the limit at which the game ends 
    returns:
    none
    '''
    # I originally misinterprited this as we were supposed to take an input instead of having this be just a loop, the code from that first
    #attempt is whats commented out
    limit = n
    game_over = False
    while game_over == False:
        #original attempt took user input for each number so if you want to play with a buddy its possible
        #guess = input('Enter a number:')
        #guess_is_number = guess.isdigit()
        #if guess_is_number == True: 
            #if isinstance(guess, float) == True or isinstance(guess, int) == True:
            #guess = float(guess)
            #if 1<= guess <= limit:
                #divide_3 = guess%3
                #divide_5 = guess%5
                #if divide_3 == 0 and divide_5 == 0:
                    #print('fizzbuzz\nGame over!')
                    #game_over = True
                    #break
                #if divide_3 == 0:
                    #print("fizz")
                #if divide_5 == 0:
                    #print('buzz')
                #if divide_5 != 0 and divide_3 != 0:
                    #print(guess)
        #anyways here how the code was supposed to be in the first place:
        #checks to see if the limit is a valid input and handles the game accordingly
        if isinstance(limit, float) == True or isinstance(limit, int) == True:
            for i in range(limit):
                i+=1
                divide_3 = i%3
                divide_5 = i%5
                if divide_3 == 0 and divide_5 == 0:
                    print('fizzbuzz')
                    if i == limit:
                        print('Game over!')
                        break
                if divide_3 == 0:
                    print("fizz")
                    if i == limit:
                        print('Game over!')
                        break
                if divide_5 == 0:
                    print('buzz')
                    if i == limit:
                        print('Game over!')
                        break
                if divide_5 != 0 and divide_3 != 0:
                    print(i)
                    if i == limit:
                        print('Game over!')
                        break
            #remminant of the original program that was wrong 
            #else:
            #   print('Please enter a number that is 1< and <=', limit)
            game_over = True
        else:
            print('Please only enter a Float or Integer value. Please try again by entering the function with a proper value')
            break
    return None

#time to test.py

fb(15)

#still confused on testmod stuff.
doctest.testmod()




                    
                
                
