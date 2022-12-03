from ..aoc import get_input

print((m := sorted([sum(map(int, i.split())) for i in get_input(1).split("\n\n")]))[-1])
print(sum(m[-3:]))
