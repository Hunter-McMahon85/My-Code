# CIS 122 spring 2021 assignment 5
# Author: Hunter McMahon
# Partner: completed solo 
# Description: you find yourself trapped, then all of a sudden you hear an ominous voice, it says "do you want to play a game?"

def playwordguess():
    #declare a function to take a guess input and assign it to recent guess, also test to make sure input is only 1 char
    #in the end, the function wouldnt work with gamplay unless i had it still return strings that were >= 1, in other words they had to be returned in gameplay to work
    def guess_in():
        """
        takes an user input and returns it
            takes an user input and returns it, if the input is more than 1 charecter the fucntion informs the user
            and violates the conditionals later in gameplay() which will have it ask for a new input
            the function also ensures that the input is a string
        Args
        none
        Returns:
        intput_guess: the users guess 
        """
        input_guess = input("Enter a guess letter (blank to quit): ")
        if len(input_guess) > 1:
            print('\t > Only enter a single letter')
            return str(input_guess)
        else:
           return str(input_guess)

    #make a function to take the guess input and see if the letter is contained within the word 
    def check_occurance(guess, word):
        """
        takes an guess and sees if it appears in a word
            takes a guess and a word and uses conditionals and the "in" keyword to determine if the guess appears in the word
        Args:
        guess (str): the guess thats being tested to see if its in the word
        word (str): the word that the guess is being tested to see if its in
        Returns:
        True: the guess appears in the word
        False: the guess doesnt appear in the word
        """
        #is_it_in = guess in word
        if guess in word:
            return True
        elif guess not in word:
            return False

    #write a function to print the results onece a word has been guesseddef
    def print_results(word, matched, unmatched, guesses):
        """
        prints the results of a round once the words been guessed
           uses escape charecters to print out the final results of a round of the game
        Args:
        word (str): the word that the guess is being tested to see if its in
        matched (str): string of the letters from the users guesses that are in the word
        unmatched (str): string of the guessed letters from the users guesses that are not in the word
        guesses (int): the total number of guesses from the user
        Returns:
        none, function is void
        """
        print ("***Results*** \nWord: \t\t" + word + "\nMatched: \t" + matched + "\nUnmatched: \t" + unmatched + "\nGuesses: \t\t" + str(guesses) )
   
    #write function to handle our gameplay elements (take inputs, and calls the check occurance function to see if its in our word and print accordingly
    #said function is the game
    def gameplay():
        """
        handles the gameplay of the game
           uses conditionals in a while loop to determine the logic of the game,
           and adjust the values of whats shown to the user, it also calls the previous functions for input along with asking for input for the word
        Args:
        none
        Returns:
        none, function is void
        """
        word = input('Enter a guess word (blank to quit): ')
        past_guesses = ""
        unmatched = ""
        matched =""
        guesses_total = 0
        i=0
        while i <= len(word):
            if len(word) >0:
                guess = guess_in()
                if 1 >= len(guess) > 0:
                    if check_occurance(guess, word) == True:
                        #if the guess is in the word
                        if check_occurance(guess, past_guesses) == False:
                            #if the guess hasnt been guessed and is found
                            i  += word.count(guess)
                            past_guesses += guess
                            guesses_total += 1
                            matched += guess
                            print("\t>", guess, "found")
                            print("\t> Guesses so far:", past_guesses)
                            if i == len(word):
                                #if i == len(word), then all charecters of the word have been found and so we print results
                                print_results(word, matched, unmatched, guesses_total)
                        elif check_occurance(guess, past_guesses) == True:
                            #if the guess was already found
                            guesses_total += 1
                            print("\t>",  guess, "already guessed and found")
                            print("\t> Guesses so far:", past_guesses)
                    elif check_occurance(guess, word) == False:
                        #if the guess is not in the word
                        if check_occurance(guess, past_guesses) == False:
                            #if the guess hasnt been guessed and isnt found
                            past_guesses += guess
                            guesses_total +=1
                            unmatched += guess
                            print("\t>", guess, " not found")
                            print("\t> Guesses so far:", past_guesses)
                        elif check_occurance(guess, past_guesses) == True:
                            #guess was already tried and not found
                            guesses_total += 1
                            print("\t>",  guess, "already guessed and not found")
                            print("\t> Guesses so far:", past_guesses)
                elif len(guess) == 0:
                        #ends the loop if the use leaves the word or the guess box blank
                        break
            elif len(word) == 0:
                break
    #call the gameplay function so that when the user ask to playwordguess by calling the function, the game plays
    gameplay()
                    
#play the game
playwordguess()
