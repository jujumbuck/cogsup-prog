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
    lower_bound=1
    upper_bound=100
    #random first guess
    guess = randint(lower_bound,upper_bound)
    
    

    while True:
        print('is your number lower or higher than', guess)
        feedback = input("Enter 'higher', 'lower', or 'correct': ").lower()

        if feedback == "higher":
            lower_bound = guess+1
            guess = randint(lower_bound,upper_bound)
        elif feedback == "lower":
            upper_bound= guess-1
            guess = randint(lower_bound,upper_bound)
        elif feedback == "correct":
            print('i correctly guessed', guess)
            break
        else:
            print('pls type higher,lower or correct')

guessing()
