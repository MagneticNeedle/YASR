from ..aoc import get_input
from sortedcontainers import SortedList

r = get_input(1).split('\n')
m = SortedList()
l = 0
for i in r:
    if i:
        l += int(i)
    else:
        m.add(l)
        l = 0

print(m[-1])
print(sum(m[-3:]))
