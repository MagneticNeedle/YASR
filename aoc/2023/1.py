from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
from ..aoc_api import get_input


day_input = get_input(1).strip().split()
total = 0
for line in day_input:
    num = []
    for i in line:
        if i.isnumeric():
            if len(num) == 2:
                num[-1] = i
            else:
                num.append(i)
    if len(num):
        total += int(''.join(num))
print(total)
