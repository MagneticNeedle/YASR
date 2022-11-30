from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
from sortedcontainers import SortedSet


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        only_win = defaultdict(lambda: True)
        one_loss = defaultdict(lambda: [False, False])
        for w, l in matches:
            if not (r := one_loss[l])[0] and not r[1]:
                r[0] = True
                r[1] = True
            elif r[0]:
                r[0] = False
            only_win[l] = False

        ret = [SortedSet(), SortedSet()]
        for w, l in matches:
            if one_loss[l][0]:
                ret[1].add(l)
            if only_win[w]:
                ret[0].add(w)

        return ret

