from karel.stanfordkarel import *

"""
Karel finishes the jigsaw puzzle:
1. Move to the last puzzle piece and pick it up.
2. Move it to the empty spot in the puzzle and put it down.
3. Return to the starting corner, facing East.
"""

def main():
    go_to_piece()
    put_piece_in_place()
    return_home()

def go_to_piece():
    # Start at (1,1) facing East, go to (3,1)
    move()
    move()
    pick_beeper()

def put_piece_in_place():
    # Currently at (3,1) facing East, need to reach (4,3)
    move()          # (4,1)
    turn_left()     # face North
    move()          # (4,2)
    move()          # (4,3)
    put_beeper()

def return_home():
    # Currently at (4,3) facing North, return to (1,1) facing East
    turn_around()   # face South
    move()          # (4,2)
    move()          # (4,1)
    turn_right()    # face West
    move()          # (3,1)
    move()          # (2,1)
    move()          # (1,1)
    turn_around()   # face East

# Helper functions
def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# Do not edit below this line
if __name__ == '__main__':
    main()
