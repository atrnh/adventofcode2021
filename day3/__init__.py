"""Advent of Code 2021: Day 3"""

from typing import List, Any
from statistics import mode


def transpose(mtx: List[List[int]]) -> List[List[int]]:
    # Modified from https://docs.python.org/3.9/tutorial/datastructures.html?highlight=transpose#nested-list-comprehensions
    return [[row[i] for row in mtx] for i in range(len(mtx[0]))]


def get_modes(mtx: List[List[int]]) -> List[int]:
    return [mode(row) for row in mtx]


def toggle_bits(bits: List[int]) -> List[int]:
    return [n ^ 1 for n in bits]


def to_dec(bits: List[int]) -> int:
    return int("".join(str(n) for n in bits), base=2)
