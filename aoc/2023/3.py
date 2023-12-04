from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
import string
from math import *
import re
from ..aoc_api import get_input

day_input = get_input(3).strip().splitlines()
CHARS = string.punctuation.replace('.', '')
NUMBERS = [list(re.finditer(r'(\d+)', line)) for line in day_input]
SYMBOLS = {}


def get_symbol_from_number(y, match: re.Match):
    for yy in [y - 1, y, y + 1]:
        for xx in range(match.start() - 1, match.end() + 1):
            if (
                    0 <= yy < len(day_input)
                    and 0 <= xx < len(day_input[0])
                    and day_input[yy][xx] in CHARS
            ):
                return yy, xx


def enumerate_all_symbols():
    for y, line in enumerate(NUMBERS):
        for match in line:
            if symbol := get_symbol_from_number(y, match):
                SYMBOLS.setdefault(symbol, []).append(int(match[1]))


def p1():
    return sum(sum(parts) for parts in SYMBOLS.values())


def p2():
    return sum(
        prod(parts)
        for (y, x), parts in SYMBOLS.items()
        if day_input[y][x] == '*' and len(parts) == 2
    )


enumerate_all_symbols()
print(p1())
print(p2())
