"""Advent of Code 2021: Day 1"""

from typing import List, Iterable, Callable, Any

from collections import deque
import itertools


def do_with_next(iterable: Iterable, func: Callable[[Any, Any], Any]):
    results = []

    prev = None
    for el in iterable:
        if prev is not None:
            results.append(func(prev, el))

        prev = el

    return results


def moving_sum(iterable, n=3):
    # This is a slightly modified version of https://docs.python.org/3/library/collections.html#:~:text=def%20moving_average(iterable,elem)%0A%20%20%20%20%20%20%20%20yield%20s%20/%20n

    it = iter(iterable)
    d = deque(itertools.islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s


def count_depth_incr(depths: List[int]) -> int:
    increases = [
        1 if is_increased else 0
        for is_increased in do_with_next(depths, lambda x, y: x < y)
    ]
    return sum(increases)


def count_rolling_depth_incr(depths: List[int]) -> int:
    rolling_depths = moving_sum(depths)
    return count_depth_incr(rolling_depths)
