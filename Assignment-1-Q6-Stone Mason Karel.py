from karel.stanfordkarel import *

def main():
    """
    universal program for repairing a wall
    """
    while front_is_clear():
        turn_left()
        case_1_clear_upward()
    case_2_blocked_upward()

def case_1_clear_upward():
        if front_is_clear():
            make_wall()
            reach_to_make_next_wall()
        else :
            turn_left()
            if no_beepers_present():
                put_beeper()
            else:
                while front_is_clear():
                    move()

def case_2_blocked_upward():
    if front_is_blocked():
        turn_left()
        if front_is_clear():
            make_wall()
            reach_to_make_next_wall()
        else :
            if no_beepers_present():
                put_beeper()
            else:
                turn_right()
                while front_is_clear():
                    move()

def make_wall(): #for making a wall and come back
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
        if no_beepers_present():
            put_beeper()
        if front_is_blocked():
            turn_left()
            turn_left()
            while front_is_clear():
                move()
                if no_beepers_present():
                    put_beeper()

def reach_to_make_next_wall():  # to reach towards next point
    turn_left()
    if front_is_clear():
        for i in range(4):
            move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
