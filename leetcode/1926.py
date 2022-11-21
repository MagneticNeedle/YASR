from typing import List
import queue


class Solution:
    dimensions = None

    def __is_exit(self, r, c):
        return r * c == 0 or r == self.dimensions[0] - 1 or c == self.dimensions[1] - 1

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        self.dimensions = len(maze), len(maze[0])
        visited = [[False for c in range(self.dimensions[1])] for r in range(self.dimensions[0])]
        paths = queue.Queue()
        paths.put([*entrance, 0])
        visited[entrance[0]][entrance[1]] = True
        dir_r = [-1, +1, 0, 0]
        dir_c = [0, 0, +1, -1]
        while paths.qsize():
            r, c, d = paths.get()

            for i in range(4):

                rr = r + dir_r[i]
                cc = c + dir_c[i]
                if (-1 < rr < self.dimensions[0] and -1 < cc < self.dimensions[1]) \
                        and (not visited[rr][cc]) \
                        and maze[rr][cc] != "+":
                    if self.__is_exit(rr, cc):
                        return d + 1
                    paths.put([rr, cc, d+1])
                    visited[rr][cc] = True

        return -1
