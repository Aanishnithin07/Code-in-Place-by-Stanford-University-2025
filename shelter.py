from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# Karel moves out of the house,
# picks up the beeper (food),
# and then returns home.

def main():
    go_to_beeper()
    pick_beeper()
    go_home()

def go_to_beeper():
    """Move from starting corner to the beeper outside the door."""
    turn_right()
    move()
    turn_left()
    move()
    move()
    move()

def go_home():
    """Return from the beeper back to the starting corner."""
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()

def turn_right():
    """Turn right using three left turns."""
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    """Turn 180 degrees."""
    turn_left()
    turn_left()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
