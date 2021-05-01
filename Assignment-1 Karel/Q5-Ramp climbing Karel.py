from karel.stanfordkarel import *

def main():
    """
    Karel should be able to draw a line with slope 1/2 in any odd sized world
    """
    put_beeper()
    while front_is_clear():
        climb_the_ramp()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def climb_the_ramp():
    move()
    move()
    turn_left()
    move()
    put_beeper()
    turn_right()

if __name__ == '__main__':
    run_karel_program('RampKarel1.w')
