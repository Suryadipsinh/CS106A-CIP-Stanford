from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():

    """
    Puting beeper at missing place to complete the puzzle
    and returning Karel to her initial position.
    """
    move()
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_right()
    turn_right()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    run_karel_program('Puzzle.w')
