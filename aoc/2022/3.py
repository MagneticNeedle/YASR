from ..aoc_api import get_input
from sortedcontainers import SortedList, SortedSet
from collections import defaultdict, Counter
from itertools import chain
from string import ascii_letters

day_input =  get_input(3).strip().split("\n")
print(
    sum(
        [
            ascii_letters.index(j) + 1
            for i in range(0, len(day_input), 3)
            for j in set(day_input[i]).intersection(
                day_input[i + 1], day_input[i + 2]
            )
        ]
    )
)
# is copilot on ?  
