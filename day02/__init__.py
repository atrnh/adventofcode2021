"""Advent of Code 2021: Day 2"""

from typing import Tuple


def tokenize(line: str) -> Tuple[str, int]:
    command, value = line.split(" ")
    return (command, int(value))


def handle_forward(value: int, *submarine_params) -> Tuple:
    x, y, *rest = submarine_params
    return x + value, y, *rest


def handle_down(value: int, *submarine_params) -> Tuple:
    x, y, *rest = submarine_params
    return x, y + value, *rest


def handle_up(value: int, *submarine_params) -> Tuple:
    x, y, *rest = submarine_params
    return x, y - value, *rest


def handle_aim_forward(value: int, *submarine_params) -> Tuple:
    x, y, aim, *rest = submarine_params
    return x + value, y + (aim * value), aim, *rest


def handle_aim_down(value: int, *submarine_params) -> Tuple:
    x, y, aim, *rest = submarine_params
    return x, y, aim + value, *rest


def handle_aim_up(value: int, *submarine_params) -> Tuple:
    x, y, aim, *rest = submarine_params
    return x, y, aim - value, *rest


handlers = {"forward": handle_forward, "down": handle_down, "up": handle_up}
aim_handlers = {
    "forward": handle_aim_forward,
    "down": handle_aim_down,
    "up": handle_aim_up,
}
