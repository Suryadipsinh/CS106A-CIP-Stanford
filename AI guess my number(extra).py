"""
Number Guesser Program

This is an example of how to use variables to
keep track of information in a program that
also makes use of loops

In this program, user will guess a number and AI will find it.
"""
import random

MIN = 0
MAX = 100

def main():
    # asking user to guess a random number
    print("Please choose a number between " +str(MIN)+ " and "+str(MAX)+ " and remember it.")

    print('')
    lower_limit = MIN
    upper_limit = MAX
    count = 0
    while True :
        count += 1
        guess = random.randint(lower_limit, upper_limit)
        # telling the number guessed by AI
        print("Is your number", guess, "?")
        # asking the user whether the number is correct or not.
        ans = input("Is it the right number ? please type correct, too low or too high : ")

        if ans == 'too high':
            # if the number is too high then we will decrease the higher limit
            upper_limit = guess - 1
        if ans == 'too low':
            # if number is too low then we will increase the lower limit
            lower_limit = guess + 1
            # for correct guess we will move out of the loop
        if ans == 'correct':
            break

    print('')
    print('')
    print("Wohooo ... I found it")
    print("I win! It took me", count, "guesses")


if __name__ == "__main__":
    main()
    
