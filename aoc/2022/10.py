from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
from ..aoc import get_input

day_input = """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".strip().split('\n')
def update_crt(cycle, pos, crt):
    r,c = divmod(cycle, 40)
    if pos-1 <= c <= pos+1:
        crt[r][c] = '#'


def print_crt(crt):
    for r in crt:
        print(*r)

day_input =  get_input(10).strip()
day_input = day_input.split('\n')
cycle  = 0
pos = 1
crt = [['.' for i in range(39)] for i in range(6)]

x = 1
ss = 0
nth_cycle = 20
max_nth_cycle = inf
for ins in day_input:
    match ins[0]:
        case 'n':
            update_crt(cycle, pos, crt)
            cycle += 1
        case 'a':
            for i in range(1,3):
                update_crt(cycle, pos, crt)
                cycle += 1
            val = int(ins.split()[1])
            pos += val
        # print(nth_cycle)

            
print_crt(crt)



