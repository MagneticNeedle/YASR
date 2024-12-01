import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(1).strip()
print(day_input)


def parse_raw():
    left,right = [],[]
    for _ in day_input.split('\n'):
        left.append(int(_.split()[0]))
        right.append(int(_.split()[1]))
    return sorted(left),sorted(right)
def p1():
    l,r = parse_raw()
    diff = [abs(l[i] - r[i]) for i in range(len(l))]
    print(sum(diff))

    
def p2():
    l, r = parse_raw()
    c = Counter(r)
    print(sum([_ * c.get(_, 0) for _ in l]))



if __name__ == '__main__':
    print(p1())
    print(p2())

