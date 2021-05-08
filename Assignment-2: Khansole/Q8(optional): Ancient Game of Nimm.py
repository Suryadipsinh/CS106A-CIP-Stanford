"""
Game starts with 20 stones 
between 2 players.
player can only take either 1 or 2 stones at a time
Last player to take stone loses.
"""

import random

def main():
    # total number of stones availabel
    stones = 20
    # initialising the player
    player = 1

    while stones > 0 :

        print("There are "+ str(stones)+ " stones left")
        # Taking user input as number of stones 
        user_input = int(input("Player " +str(player)+ " would you like to remove 1 or 2 stones? "))
        # Checking the value is invalid or not
        while user_input <= 0 or user_input > 2 :
            user_input = int(input("Please enter 1 or 2: "))
        # Calculating number of stones after each turn 
        stones -= user_input
        # Printing a new line
        print('')
        # Changing a player after each turn
        if player == 1 :
            player += 1
        else:
            player = player - 1
    # Printing a winnner for the game
    print("Player "+str(player) +" wins!")

if __name__ == '__main__':
    main()
