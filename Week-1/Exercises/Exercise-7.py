"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""

from random import randint



print("think of a number between 1 and 100")


def guessing():
    #creating upper and lower bounds to have the range of the guess
    lower_bound=1 
    upper_bound=100
    #random first guess
    guess = randint(lower_bound,upper_bound)
    
    

    while True:
        print('is your number lower or higher than', guess)
        feedback = input("Enter 'higher', 'lower', or 'correct': ").lower() #asking user to enter feedback about guess

        if feedback == "higher":
            lower_bound = guess+1 #updating lower bound to be in the range of previous guess but higher
            guess = randint(lower_bound,upper_bound) #guessing a random number in the bound of the last guess+1 up to the upper bound whoch hasnt changed
        elif feedback == "lower":
            upper_bound= guess-1 #updating upper bound to be in the range of previous guess but lower
            guess = randint(lower_bound,upper_bound) #guessing a random number in the range of the lower bound that hasnt changed up to the previous guess -1
        elif feedback == "correct":
            print('i correctly guessed', guess) 
            break #break loop so that the guessing stops because correct
        else:
            print('pls type higher,lower or correct')

guessing()
