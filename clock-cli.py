#! /usr/bin/env python3

import os
import time
import datetime

"""
* TODO 타이머 기능
* TODO 알람 기능
"""


ZERO = ( "#####", "#   #", "#   #", "#   #", "#####",)
ONE = ( " ##  ", "  #  ", "  #  ", "  #  ", " ### ",)
TWO = ( "#####", "    #", "#####", "#    ", "#####",)
THREE = ( "#####", "    #", "#####", "    #", "#####",)
FOUR = ( "#   #", "#   #", "#####", "    #", "    #",)
FIVE = ( "#####", "#    ", "#####", "    #", "#####",)
SIX = ( "#####", "#    ", "#####", "#   #", "#####",)
SEVEN = ( "#####", "    #", "    #", "    #", "    #",)
EIGHT = ( "#####", "#   #", "#####", "#   #", "#####",)
NINE = ( "#####", "#   #", "#####", "    #", "    #",)
DOTS = ( "  ", "##", "  ", "##", "  ",)

DIGITS = ( ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def get_now():
    """Get the time"""
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    return hour, minute, second


def print_big_clock(t:tuple) -> None:
    ...

def print_small_clock(t:tuple) -> None:
    hour = t[0]
    minute = t[1]
    second = t[2]

    if hour < 10:
        hour = "0" + str(t[0])
    if minute < 10:
        minute = "0" + str(t[1])
    if second < 10:
        second = "0" + str(t[2])

    print(f"{hour}:{minute}:{second}")

def print_time(t:tuple, big=False) -> None:
    """Print the time on cli"""
    if big:
        print_big_clock(t)
    else:
        print_small_clock(t)


def main():
    while True:
        try:
            os.system('clear')
            now = get_now()
            print_time(now)
            time.sleep(1)
        except EOFError:
            print("Bye")

if __name__ == "__main__":
    main()
