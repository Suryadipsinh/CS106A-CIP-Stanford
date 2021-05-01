from karel.stanfordkarel import *

def main():
    """
    Making Chess Board with Karel.
    """
    for i in range(3):
        move_3()
        paint_corner(GREEN)
        take_left_turn()
        move_3()
        paint_corner(GREEN)
        take_right_turn()
    move_3()
    paint_corner(GREEN)
    take_left_turn()
    move_3()
    paint_corner(GREEN)
    move()
    turn_right()
    turn_right()

def take_right_turn():
        move()
        turn_right()
        move()
        turn_right()
def take_left_turn():
        move()
        turn_left()
        move()
        turn_left()
def move_3():
        for i in range(3):
            paint_corner(GREEN)
            move()
            move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
