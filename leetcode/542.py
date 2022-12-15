from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


def print_grid(grid: List[List[int]]):
    for i in grid:
        print(*i)
    print("<====>")


class Solution:  
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else inf
                    left = mat[r][c - 1] if c > 0 else inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else inf
                    right = mat[r][c + 1] if c < n - 1 else inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat