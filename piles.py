from karel.stanfordkarel import *

# File: piles.py
# -----------------------------
# Karel picks up all the beepers on the first row.

def main():
    while front_is_clear():
        pick_all_beepers()
        move()
    pick_all_beepers()   # pick beepers on the last corner

def pick_all_beepers():
    while beepers_present():
        pick_beeper()

# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()
