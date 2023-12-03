from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect
from ..aoc_api import get_input


day_input =  get_input(8).strip().split("\n")
r,c = len(day_input), len(day_input[0])
visible_trees = r*2 + c*2 - 4

def p1(day_input):

    for i in range(1, r-1):
        for j in range(1, c-1):
            tree = int(day_input[i][j])

            conditions = [
                int(max(day_input[i][:j], key=lambda x: int(x))) < tree,
                int(max(day_input[i][j+1:], key=lambda x: int(x))) < tree,
        ]

            up = True
            for ii in range(0, i):
                if int(day_input[ii][j]) >= tree:
                    up = False
                    break
            down = True
            for ii in range(i+1, r):
                if int(day_input[ii][j]) >= tree:
                    down = False
                    break
            conditions.append(up or down)
            if any(conditions):
                visible_trees +=1
    return visible_trees


def p2(day_input):
    high = []
    for i in range(r):
        for j in range(c):
            tree = int(day_input[i][j])
            left,right,u,d = 0,0,0,0
            ii,jj = i-1,j-1
            while(ii >= 0 and int(day_input[ii][j]) <= tree):   
                u += 1
                if int(day_input[ii][j]) == tree:                
                    break
                ii -= 1
            ii = i+1
            while(ii < r and int(day_input[ii][j]) <= tree):
                d += 1
                if int(day_input[ii][j]) == tree:                
                    break
                ii += 1


           
            while(jj >= 0 and int(day_input[i][jj]) <= tree):
                left += 1
                if int(day_input[i][jj]) == tree:                
                    break
                jj -= 1

            jj = j+1
            while(jj < c and (int(day_input[i][jj]) <= tree)):
                right += 1
                if int(day_input[i][jj]) == tree:                
                    break
                jj += 1


           
            # print(u,left,right,d)
            high.append(left*right*u*d)
    # print(high)
    return high
            






print(max(p2(day_input)))
