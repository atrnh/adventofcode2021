"""Advent of Code 2021: Day 4

5x5 bingo

0 1 3


0  1  2  3  4
5  6  7  8  9
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24

board manager stores boards and map of numbers and where they're located
"""

import enum
from typing import List, Any, Dict, Tuple

import itertools
import re
from collections import defaultdict, UserDict


def yield_rows(boards: List[List[bool]], n: int = 5):
    for i, board in enumerate(boards):
        start = 0

        while start < len(board):
            yield i, board[start : start + n]

            start += n


def yield_columns(boards: List[List[bool]], n: int = 5):
    for i, board in enumerate(boards):
        start = 0

        while start < n:
            yield i, board[start : start + n ** 2 : n]

            start += 1


def scan_for_winner(boards: List[List[bool]]):
    for board_num, row in iter(yield_rows(boards)):
        if row and all(row):
            return board_num


class BingoNumMap(UserDict):
    def __getitem__(self, key):
        if key not in self.data:
            self.data[key] = []

        return super().__getitem__(key)

    def __setitem__(self, key, item):
        self.data[key] = item

    def update(self, map):
        for key, val in map.items():
            self[key] += val


def parse_board_data(board_str: str) -> List[int]:
    return [int(n) for n in re.split(r"\s+", board_str)]


def build_board(width: int = 5, height: int = 5) -> List[bool]:
    return [False for _ in range(width * height)]


def build_nummap(board_data: List[int]) -> Dict[int, List[Any]]:
    nummap = defaultdict(list)

    for i, n in enumerate(board_data):
        nummap[n].append(i)

    return nummap


# def mark_num(num: int, nummap: Dict[int, Tuple[Board, int]] = NUMMAP) -> None:
#     for board, i in nummap[num]:
#         board.state[i] = 1
