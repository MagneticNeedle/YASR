import math
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
from typing import List

import aoc_api

day_input = aoc_api.get_input(5).strip()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def parse_raw(raw: str):
    raw = raw.split('\n\n')
    maps = [list(map(int, raw[0].split(":")[-1].strip().split()))]

    for i in range(1, len(raw)):
        maps.append(
            [tuple(map(int, _.split())) for _ in raw[i].split(":")[-1].strip().split('\n')]
        )
    return maps
    

def p1():
    maps = parse_raw(day_input)
    seeds = maps[0]
    min_location = math.inf
    for seed in seeds:
        to_check = seed
        for factor in maps[1:]:
            for m in factor:
                if m[1] <= to_check < (m[1] + m[2]):
                    # print(f"Found {m}")
                    diff = to_check - m[1]
                    to_check = m[0] + diff
                    break
        min_location = min(min_location, to_check)
    return min_location

def p2():
    seeds, *maps = day_input.split("\n\n")
    nums = [int(x) for x in seeds.split()[1:]]
    seeds = [nums[i:i + 2] for i in range(0, len(nums), 2)]
    for rawmap in maps:
        _, *ranges = rawmap.split("\n")
        newseeds = []
        for rrange in ranges:
            to, fro, le = map(int, rrange.split())
            oldseeds = seeds
            seeds = []
            for seed_fro, seed_le in oldseeds:
                seed_to = seed_fro + seed_le
                starts_within = fro <= seed_fro < fro + le
                ends_within = fro < seed_to <= fro + le
                if starts_within and ends_within:
                    newseeds.append([seed_fro - fro + to, seed_le])
                elif starts_within:
                    over = seed_to - (fro + le)
                    newseeds.append([seed_fro - fro + to, seed_le - over])
                    seeds.append([fro + le, over])
                elif ends_within:
                    under = fro - seed_fro
                    newseeds.append([to, seed_le - under])
                    seeds.append([seed_fro, under])
                elif seed_fro < fro and seed_to > fro + le:
                    over = seed_to - (fro + le)
                    under = fro - seed_fro
                    newseeds.append([to, le])
                    seeds.append([seed_fro, under])
                    seeds.append([fro + le, over])
                else:
                    seeds.append([seed_fro, seed_le])
        seeds += newseeds

    return min(seed[0] for seed in seeds)


if __name__ == '__main__':
    print(p1())
    print(p2())
