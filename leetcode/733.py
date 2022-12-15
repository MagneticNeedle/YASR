from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int, pr=None,pc=None) -> List[List[int]]:
        if (v := image[sr][sc]) == color:
            return image
        m,n = len(image),len(image[0])
        dir_r = [-1, 1, 0, 0]
        dir_c = [0, 0, -1, 1]
        stack = [(sr, sc)]
        while len(stack):
            r,c = stack.pop()
            image[r][c] = color
            for i in range(4):
                rr = r + dir_r[i]
                cc = c + dir_c[i]
                if 0<=rr<m and 0<=cc<n and image[rr][cc] == v:
                    stack.append((rr, cc))
        return image
