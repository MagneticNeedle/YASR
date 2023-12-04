from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
import string
import re
from math import *
from ..aoc_api import get_input

day_input = get_input(4).strip().splitlines()


def get_data(line: str):
    c_id = int(line.split(':')[0].split()[-1].strip())
    parts = line.split(':')[1].split('|')
    winnings = set(map(int, parts[0].split()))
    c_nums = set(map(int, parts[1].split()))
    wins = len(winnings.intersection(c_nums))

    return c_id, wins


CARDS_COUNT = {card_id: 1 for card_id in range(1, len(day_input) + 1)}
total = 0

for line in day_input:
    card_id, number_of_winning_cards = get_data(line)

    # part one
    total += int(2 ** (number_of_winning_cards - 1))

    # part two
    for i in range(card_id + 1, card_id + number_of_winning_cards + 1):
        CARDS_COUNT[i] += 1 * CARDS_COUNT[card_id]

print(total)
print(sum(CARDS_COUNT.values()))


# golfed
A=C=0;B=[1]*999
for l in open(0):a=l.split();i,*B=B;C+=i;j=0;exec('B[j]+=i;j+=1;'*len({*a[:12]}&{*a[12:]}));A+=2**j//2
print(A,C)

