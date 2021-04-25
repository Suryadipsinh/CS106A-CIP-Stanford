from karel.stanfordkarel import *

def main():
    """
    task 2021
    placing 20 beepers, moving Karel one step,
    placing 21 beepers, and moving Karel one more step.
    
    """
    for i in range(20):
        put_beeper()
    move()
    for i in range(21):
        put_beeper()
    move()

if __name__ == '__main__':
    run_karel_program('3x3.w')
