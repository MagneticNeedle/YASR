from typing import List
import queue


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        possible_exits = []
        dimensions = len(maze), len(maze[0])
        visited = [[False for c in range(dimensions[1])] for r in range(dimensions[0])]

        for index, cell in enumerate(maze[0]):
            if cell == "." and (cell_index := [0, index]) != entrance:
                possible_exits.append(cell_index)

        for index, cell in enumerate(maze[-1]):
            if cell == "." and (cell_index := [dimensions[0]-1, index]) != entrance:
                possible_exits.append(cell_index)

        for index in range(1, dimensions[0]-1):
            if maze[index][0] == ".":
                cell_index = [index, 0]
                if cell_index != entrance:
                    possible_exits.append(cell_index)

            if maze[index][-1] == ".":
                cell_index = [index, dimensions[1]-1]
                if cell_index != entrance:
                    possible_exits.append(cell_index)

        if not possible_exits:
            return -1
        # print(f"{dimensions, possible_exits}\n")
        paths = queue.Queue()
        paths.put(entrance)
        move = 0
        nodes_in_layer = 1
        nodes_in_next_layer = 0
        dir_r = [-1, +1, 0, 0]
        dir_c = [0, 0, +1, -1]
        reached_end = False
        visited[entrance[0]][entrance[1]] = True

        def explore(r: int, c: int):
            # explore neighbours
            nonlocal nodes_in_next_layer
            for i in range(4):
                rr = r + dir_r[i]
                cc = c + dir_c[i]
                # print(f"\t{rr, cc}", end='')

                if (-1 < rr < dimensions[0] and -1 < cc < dimensions[1]) and (not visited[rr][cc]) and maze[rr][cc] != "+":
                    # print(f"\t\tValid")
                    paths.put([rr, cc])
                    visited[rr][cc] = True
                    nodes_in_next_layer += 1
                # else:
                #     print('\t\tInValid')

        while paths.qsize():
            # [print(_) for _ in visited]
            curr = paths.get()
            # print(curr)
            if curr in possible_exits:
                reached_end = True
                break
            explore(curr[0], curr[1])
            nodes_in_layer -= 1
            if nodes_in_layer == 0:
                nodes_in_layer = nodes_in_next_layer
                nodes_in_next_layer = 0
                move += 1

        if reached_end:
            return move
        return -1
