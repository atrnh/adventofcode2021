"""Advent of Code 2021: Day 4"""

import sys
import re

from . import (
    BingoNumMap,
    parse_board_data,
    build_board,
    build_nummap,
    scan_for_winner,
)

from collections import defaultdict
from itertools import compress

BOARDS = []
# Map numbers to their locations.
NUMMAP = BingoNumMap()

if __name__ == "__main__":
    inpt = sys.stdin.read()
    chosen_nums, *raw_boards = inpt.strip().split("\n\n")

    boards_data = [parse_board_data(raw.strip()) for raw in raw_boards]

    for board_data in boards_data:
        board = build_board()
        BOARDS.append(board)

        local_nummap = build_nummap(board_data)
        NUMMAP.update(
            {
                key: [(board, i) for i in locations]
                for key, locations in local_nummap.items()
            }
        )

    for num in [int(n) for n in chosen_nums.split(",")]:
        locations = NUMMAP[num]

        for board, i in locations:
            board[i] = True

        winner = scan_for_winner(BOARDS)
        if winner:
            win_board = boards_data[winner]
            unmarked_nums = compress(
                win_board, [not is_marked for is_marked in BOARDS[winner]]
            )

            score = sum(unmarked_nums) * num
            print(score)
            break
