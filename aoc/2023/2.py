from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
import math, re
from ..aoc_api import get_input

day_input = get_input(2).strip()
# Part 1
RED, GREEN, BLUE = 12, 13, 14
total = 0
for line in day_input.splitlines():
    game_id = int(re.findall(r'^Game (\d+):', line)[0])
    blue_dices = [int(x) for x in re.findall(r'(\d+) blue', line)]
    red_dices = [int(x) for x in re.findall(r'(\d+) red', line)]
    green_dices = [int(x) for x in re.findall(r'(\d+) green', line)]

    if any(r > RED for r in red_dices) or any(b > BLUE for b in blue_dices) or any(g > GREEN for g in green_dices):
        continue
    total += game_id
print(total)
# Part 2
print(
    sum(
        [
            math.prod(
                map(
                    lambda k: max([int(x) for x in re.findall(rf"(\d+) {k}", _)]), "rgb"
                )
            )
            for _ in day_input.splitlines()
        ]
    )
)

# Code golfed
*I, = open(t := 0)
i = 1
for l in I:
    for s in l.replace(*';,').split(','):
        a = s.split()
        if int(a[-2]) > 24 - ord(a[-1][0]) // 9: break
    else:
        t += i
print(sum(math.prod(max(map(int, re.findall(r"(\d+) " + x, l))) for x in "rgb") for l in I))
