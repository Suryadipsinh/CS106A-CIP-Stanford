from karel.stanfordkarel import *

def main():
    for i in range(3):
        make_wave()
        move()
        move()
    make_wave()
# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()

def make_wave():
    put_beeper()
    move()
    turn_left()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    turn_right()
    move()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
