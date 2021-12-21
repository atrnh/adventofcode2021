"""Advent of Code 2021: Day 3"""

import sys

from . import (
    transpose,
    get_modes,
    toggled_bits,
    to_dec,
    build_rating_calculator,
)

if __name__ == "__main__":
    # Create matrix
    inpt = [[int(n) for n in line.strip()] for line in sys.stdin.readlines()]

    gamma_bits = get_modes(transpose(inpt))
    epsilon_bits = toggled_bits(gamma_bits)

    # Part 1
    print(to_dec(gamma_bits) * to_dec(epsilon_bits))

    # Part 2
    calculate_oxy = build_rating_calculator(lambda most, _: most, default=1)
    calculate_co2 = build_rating_calculator(lambda _, least: least, default=0)

    oxy = calculate_oxy(inpt)
    co2 = calculate_co2(inpt)

    print(to_dec(oxy) * to_dec(co2))
