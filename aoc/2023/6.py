import math
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import numpy
import aoc_api

day_input = aoc_api.get_input(6).strip()
print(day_input[:100])


def parse_raw(raw: str):
    raw = raw.splitlines()
    race_time = map(int, raw[0].split(':')[-1].strip().split())
    distance = map(int, raw[1].split(':')[-1].strip().split())
    return race_time, distance

# old p1
    # for race_time, d in zip(*parse_raw(day_input)):
    # wins_this = 0
    # prev = 0
    # for time_held in range(race_time+1):
    #     dc = (race_time-time_held) * time_held
    #     if dc > d:
    #         wins_this += 1
    #         prev = dc
    #     elif dc < prev:
    #         break


def p1():

    return math.prod(
        numpy.diff(
            numpy.roots([1, race_time, distance]).astype(int)
        ).item() for race_time, distance in zip(*parse_raw(day_input))
    )


def p2():
    # first approach brute force using P1 solution
    # removed
    return numpy.diff(numpy.roots([1, 50748685, 242101716911252]).astype(int)).item()


if __name__ == '__main__':
    print(p1())
    print(p2())
