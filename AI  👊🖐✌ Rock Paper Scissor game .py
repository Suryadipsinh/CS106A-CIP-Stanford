"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition 
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors. 
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3

def main():
    print_welcome()
    score = 0
    for i in range(N_GAMES):
        human_move = get_human_move()
        ai_move = get_ai_move()
        winner = get_winner(human_move, ai_move)
        declare_result(ai_move, winner)
        score += get_score(winner)
    print("Your score is ", score)
    

def get_score(winner):
    """
    You get 1 point for winning, and lose 1 point for losing.
    >>> get_score('tie')
    0
    >>> get_score('human')
    1
    >>> get_score('ai')
    -1
    """
    if winner == 'human':
        return +1
    if winner == 'ai':
        return -1
    return 0

def declare_result(ai_move, winner):
    """
    Lets the user about moves of AI and result of the game.
    """
    print("The AI plays ", ai_move)
    if winner == 'Tie':
        print("There is tie !")
    else:
        print("Winner was", winner)
    print('')

def get_human_move():
    # getting moves of human 
    while True:
        human_move = input("What do you play ? ")
        if is_valid_move(human_move):
            return human_move
        print("Enter a valid move")

def is_valid_move(move):
    # for checking the valid move
    """
    parameter move: string repersenting what the user enter 
    return: boolean which is true if the move was valid
    >>> is_valid_move('rock')
    True
    >>> is_valid_move('unicoen')
    False
    >>> is_valid_move('paper')
    True
    >>> is_valid_move('scissors')
    True
    """
    if move == 'rock':
        return True
    if move == 'paper':
        return True
    if move == 'scissors':
        return True
    return False 

def get_ai_move():
    # for move of ai
    move = random.randint(1, 3)
    if move == 1:
        return 'rock'
    if move == 2:
        return 'paper'
    return 'scissors'

def get_winner(human_move, ai_move):
    """
    return: either 'ai' or 'human'
    >>> get_winner('rock', 'paper')
    'AI'
    >>> get_winner('rock', 'scissor')
    'human'
    >>> get_winner('rock', 'rock')
    'Tie'
    >>> get_winner('scissors', 'paper')
    'human'
    """
    if human_move == ai_move:
        return 'Tie'
    if human_move == 'rock':
        if ai_move == 'paper':
            return 'AI'
        return 'human'
    if human_move == 'paper':
        if ai_move == 'rock':
            return 'human'
        return 'AI'
    if human_move == 'scissors':
        if ai_move == 'rock':
            return 'AI'
        return 'human'

def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')

if __name__ == '__main__':
    main()
