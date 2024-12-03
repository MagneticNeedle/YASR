import math
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(3).strip()

def parse_raw(pattern: str):
    return re.findall(pattern, day_input)


    
def p1():
    pairs = sum([(int(a)*int(b)) for a, b in parse_raw(r"mul\((\d+),\s*(\d+)\)")])
    print(pairs)

    
def p2():
    sum_ = 0
    do = True
    for instruction in parse_raw(r"do\(\)|don't\(\)|mul\(\d+,\d+\)"):
        if do and (capture := re.findall(r"mul\((\d+),\s*(\d+)\)", instruction)):
            sum_ += prod(map(int, capture[0]))
        else:
            do = instruction == "do()"
    return sum_


if __name__ == '__main__':
    # print(p1())
    print(p2())

