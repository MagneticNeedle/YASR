from ..aoc import get_input

l = 0
d = get_input(6).strip()
while 1:
    if len(set(d[l:l+14])) == 14:
        print(l+14)
        break
    l += 1
