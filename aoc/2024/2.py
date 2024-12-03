import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(2).strip()

"""
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""
def parse_raw():
    inp = []
    for _ in day_input.split('\n'):
        inp.append(list(map(int, _.split())))
    return inp

def check_report(row: list) -> bool:
    direction = row[1] - row[0]
    for i in range(1, len(row)):
        diff = row[i] - row[i - 1]
        if not (1<=abs(diff)<=3 and diff * direction > 0):
            return False
    return True

def p1():
    inp = parse_raw()
    return sum([check_report(report) for report in inp])


def p2():
    inp = parse_raw()
    safe = 0
    for report in inp:
            safe += True in [check_report(report[:i] + report[i + 1:]) for i in range(len(report))]
    return safe

if __name__ == '__main__':
    print(p1())
    print(p2())

