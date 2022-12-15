from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        left, right = [], []
        for i in intervals:
            if i[1] < newInterval[0]:
                left += [i]
            elif i[0] > newInterval[1]:
                right += [i]
            else:
                newInterval = [min(newInterval[0], i[0]), max(newInterval[1], i[1])]
        return left + [newInterval] + right
