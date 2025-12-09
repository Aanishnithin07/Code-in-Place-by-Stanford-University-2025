from karel.stanfordkarel import *

"""
Karel places 20 beepers, moves forward,
places 24 beepers, then moves forward again,
ending facing East.
"""

def main():
    # Place 20 beepers
    for i in range(20):
        put_beeper()
    
    move()
    
    # Place 24 beepers
    for i in range(24):
        put_beeper()
    
    move()

# Do not edit below
if __name__ == '__main__':
    main()
