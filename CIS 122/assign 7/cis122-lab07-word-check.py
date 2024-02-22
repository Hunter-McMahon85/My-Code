# CIS 122 spring 2021 lab 7 word check
# Author: Hunter McMahon
# Partner: completed solo during lab session
# Description: *playing a scrabble game* wait thats not a word *dictionary flipping intensifies*



#take input (use a loop)
#temp variable to signal that we still want input
def find_word():
    """
    takes a user word input and checks to see if its on the word list
        uses loops and booleans to check and see if an given word is on a list of words 
    Args
    none 
    Returns:
    none: void function
    """
    ask_for_word = True
    while ask_for_word == True:
        #ask for input
        user_word = input('Enter a search word (blank to exit):')
        user_word = user_word.strip()
        #determine if we recieved an input
        if len(user_word) == 0:
            ask_for_word == False
            break
        elif len(user_word) > 0:
            ask_for_word = True
            #search to see if the users word is int the word list
            fin = open('words_alpha.txt')
            word_found = False
            #loop goes through the words list and test to see if the word in each line is the same as the input
            #if the words match word_found is set to true and the found result is printed
            #if the words dont match the not found result is printed
            for line in fin:
                line = line.strip()
                if user_word.lower() == line.lower():
                    word_found = True
                    break
                else:
                    word_found = word_found
            if word_found == True:
                print('Word', user_word, 'found')
            elif word_found == False:
                print('Word', user_word, 'not found')
find_word()
