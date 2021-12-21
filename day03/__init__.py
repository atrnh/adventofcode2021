"""Advent of Code 2021: Day 3"""

from typing import List, Callable
from statistics import mode
from collections import Counter
from itertools import chain, compress


def transpose(mtx: List[List[int]]) -> List[List[int]]:
    # Modified from https://docs.python.org/3.9/tutorial/datastructures.html?highlight=transpose#nested-list-comprehensions
    return [[row[i] for row in mtx] for i in range(len(mtx[0]))]


def get_modes(mtx: List[List[int]]) -> List[int]:
    return [mode(row) for row in mtx]


def toggled_bits(bits: List[int]) -> List[int]:
    return [n ^ 1 for n in bits]


def to_dec(bits: List[int]) -> int:
    return int("".join(str(n) for n in bits), base=2)


def calculate_crit(
    bits: List[int], criterion: Callable[[int, int], int], default: int
) -> int:
    most, most_count, least, least_count = chain.from_iterable(
        Counter(bits).most_common()
    )

    return criterion(most, least) if most_count != least_count else default


def build_rating_calculator(
    criterion: Callable[[int, int], int], default: int
) -> Callable[[List[List[int]]], int]:
    def calculate_rating(mtx: List[List[int]]) -> int:
        candidates = mtx[:]
        i = 0

        while len(candidates) > 1:
            transposed = transpose(candidates)
            bits = transposed[i]
            crit = calculate_crit(bits, criterion, default)

            candidates = list(
                compress(candidates, bits if crit else toggled_bits(bits))
            )
            i += 1

        return candidates[0]

    return calculate_rating
