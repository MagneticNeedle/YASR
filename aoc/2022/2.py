from ..aoc import get_input

day_input = [
    ("ABC".index(move[0]), "XYZ".index(move[2])) for move in
    get_input(2).strip().split('\n') ]

print(sum(3*((m2 - m1 + 1)%3) + m2 + 1 for m1, m2 in day_input))
print(sum((m1 + m2 - 1)%3 + 1 + m2 * 3 for m1, m2 in day_input))
