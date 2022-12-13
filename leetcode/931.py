from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(0, n):
                matrix[i][j] += min(matrix[i-1][j], matrix[i-1][max(0, j-1)], matrix[i-1][min(n-1, j+1)])
        return min(matrix[-1])
