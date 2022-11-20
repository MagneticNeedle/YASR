# https://leetcode.com/problems/erect-the-fence/
from typing import List
from math import sqrt, atan2

"""
Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
"""


def polar_angle(start: list, end: list) -> float:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return atan2(dy, dx)


def dist(start: list, end: list) -> float:
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    return sqrt((pow(dx, 2) + pow(dy, 2)))


def orientation(p1, p2, p3) -> float:

    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])


class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) <= 3:
            return trees

        trees.sort(key=lambda x: (x[1], x[0]))
        p0 = trees[0]

        trees.sort(key=lambda p: (polar_angle(p0, p), dist(p0, p)))
        l = polar_angle(p0, trees[-1])
        r = []
        for i in trees[::-1]:
            if polar_angle(p0, i) == l:
                r.append(i)
        if rl := len(r):
            trees[len(trees)-rl:] = r
        hull = []
        for tree in trees:
            while len(hull) >= 2 and not orientation(hull[-2], hull[-1], tree) <= 0:
                hull.pop()
            hull.append(tree)
        return hull


# if __name__ == '__main__':
#     trees = [[0,2],[0,1],[0,0],[1,0],[2,0],[1,1]]
#
#     # print(orientation([1, 3], [1, 2], [2, 1],))
#     p = Solution().outerTrees(trees)
#     print([tuple(i) for i in p])
