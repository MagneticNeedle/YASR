from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not len(nums): return 0
        p1,p2 = 0,0
        for i in nums:
            tmp = p1
            p1 = max(p2+i, p1)
            p2 = tmp
            print(p2, p1, i)
        
        return p1