# this script is a solution to Advent of Code 2022, day 4

from ..aoc_api import get_input

day_input = get_input(4).split('\n')
total_items = len(day_input)
m = 0
for i in range(total_items):
    l,r = (list(map(int,i.split('-'))) for i in day_input[i].split(','))
    if r[0] <= l[1] and r[1] >= l[0]:
        m += 1
print(m)

