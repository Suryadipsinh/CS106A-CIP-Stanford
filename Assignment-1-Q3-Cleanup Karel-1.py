from karel.stanfordkarel import *

def main():
    """
    Karel should be able to
    pick up a beeper from the current position if one is present.
    (but do nothing if no beepers are present)
    """
    check_beeper()

def check_beeper():
    if beepers_present():
        pick_beeper()

if __name__ == '__main__':
    run_karel_program('SafePickup2.w')
