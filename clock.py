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
    LINES = 5
    SPACES = " "
    hour = f"{t[0]:02}"
    minute = f"{t[1]:02}"
    second = f"{t[2]:02}"

    h_digits = (DIGITS[int(hour[0])], DIGITS[int(hour[1])])
    m_digits = (DIGITS[int(minute[0])], DIGITS[int(minute[1])])
    s_digits = (DIGITS[int(second[0])], DIGITS[int(second[1])])

    for l in range(LINES):
        line = h_digits[0][l] + SPACES + h_digits[1][l] + SPACES + DOTS[l] + SPACES +\
               m_digits[0][l] + SPACES + m_digits[1][l] + SPACES + DOTS[l] + SPACES +\
               s_digits[0][l] + SPACES + s_digits[1][l]
        print(line)


def print_small_clock(t:tuple) -> None:
    hour = t[0]
    minute = t[1]
    second = t[2]

    print(f"{hour:02}:{minute:02}:{second:02}")


def print_time(t:tuple, big=False) -> None:
    """Print the time on cli"""
    if big:
        print_big_clock(t)
    else:
        print_small_clock(t)


def main(big=False):
    while True:
        os.system('clear')
        now = get_now()
        print_time(now, big=big)
        time.sleep(1)


if __name__ == "__main__":
    main(True)
