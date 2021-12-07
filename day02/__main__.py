"""Advent of Code 2021: Day 2"""

import sys

from . import tokenize, handlers, aim_handlers

if __name__ == "__main__":
    inpt = [tokenize(line) for line in sys.stdin.readlines()]

    # Part 1
    submarine1 = 0, 0
    for command, value in inpt:
        handler = handlers[command]

        submarine1 = handler(value, *submarine1)

    x, y = submarine1
    print(x * y)

    # Part 2
    submarine2 = 0, 0, 0
    for command, value in inpt:
        handler = aim_handlers[command]

        submarine2 = handler(value, *submarine2)

    x, y, *_ = submarine2
    print(x * y)
