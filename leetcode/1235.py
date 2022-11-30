from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        mapping = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = defaultdict(int)
        dp[0] = 0
        return mapping