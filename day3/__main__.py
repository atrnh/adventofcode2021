"""Advent of Code 2021: Day 3"""

import sys

from . import transpose, get_modes, toggle_bits, to_dec

if __name__ == "__main__":
    # Create matrix
    inpt = transpose(
        [[int(n) for n in line.strip()] for line in sys.stdin.readlines()]
    )

    gamma_bits = get_modes(inpt)
    epsilon_bits = toggle_bits(gamma_bits)

    # Part 1
    print(to_dec(gamma_bits) * to_dec(epsilon_bits))
