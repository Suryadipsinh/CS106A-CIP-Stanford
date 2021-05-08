from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def main():
    """
    Finding mid point 
    """
    while front_is_clear():
        a()
    turn_around()
    while left_is_clear():
        b()
    put_beeper()

def a(): # Karel will move to the corner
     turn_left()
     move()
     turn_right()
     move()
     if front_is_clear():
       move()

def b(): # Karel will move be
   move()
   turn_left()
   move()
   turn_right()

def turn_around():  # Karel will turn back
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint.w')
