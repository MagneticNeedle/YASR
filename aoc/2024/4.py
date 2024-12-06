import re
from collections import defaultdict, Counter
from functools import lru_cache
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(4).strip()

@lru_cache()
def parse_raw():
    char_map = defaultdict(lambda: '.')

    for i, line in enumerate(day_input.split('\n')):
        for j, c in enumerate(line):
            char_map[i + 1j * j] = c
    return char_map


def p1():
    char_map = parse_raw()
    k = list(char_map.keys())
    count = 0
    for d in (1, -1, 1j, -1j, 1 + 1j, 1 - 1j, -1 - 1j, -1 + 1j):
        for s in k:
            count += all([
                char_map[s] == 'X',
                char_map[s + d] == 'M',
                char_map[s + 2 * d] == 'A',
                char_map[s + 3 * d] == 'S'
            ])

    return count


def p2():
    char_map = parse_raw()
    k = list(char_map.keys())
    count = 0
    for s in k:
        count +=  all([
            char_map[s] == 'A',
            any([
                char_map[s - 1 - 1j] == 'M' and char_map[s + 1 + 1j] == 'S',
                char_map[s - 1 - 1j] == 'S' and char_map[s + 1 + 1j] == 'M'
            ]),
            any([
                char_map[s - 1 + 1j] == 'M' and char_map[s + 1 - 1j] == 'S',
                char_map[s - 1 + 1j] == 'S' and char_map[s + 1 - 1j] == 'M'
            ])
        ])

    return count


if __name__ == '__main__':
    print(p1())
    print(p2())

