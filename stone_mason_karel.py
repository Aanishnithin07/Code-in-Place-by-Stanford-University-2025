from karel.stanfordkarel import *

"""
Karel repairs the Temple of Artemis by rebuilding
all columns to a height of 5.
"""

def main():
    while front_is_clear():
        build_column()
        move_to_next_column()
    build_column()   # build last column


def build_column():
    # Build a column of height 5
    turn_left()
    for i in range(5):
        put_beeper()
        if front_is_clear():
            move()
    turn_around()
    for i in range(4):
        move()
    turn_left()


def move_to_next_column():
    # Move 4 spaces to the next column
    for i in range(4):
        move()


def turn_around():
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
