from karel.stanfordkarel import *

def main():
    """
   CleanupKarel should be able to
   pick up all beepers from the first row of any sized world and
   end in the bottom right corner facing East.
    """
    while front_is_clear():
        check_beeper()
        move()
    while front_is_blocked():
         check_beeper()
         turn_left()

def check_beeper():
    if beepers_present():
        pick_beeper()

if __name__ == '__main__':
    run_karel_program('Cleanup1.w')
