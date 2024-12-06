import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(5).strip()
# print(day_input)


def parse_raw():
    rules, updates = day_input.split('\n\n')
    return (
        [list(map(int, _.split("|"))) for _ in rules.split('\n')],
        [list(map(int, update.split(','))) for update in updates.split('\n')]
    )

    
def p1():
    rules, updates = parse_raw()
    rules_map = defaultdict(list)
    for rule in rules:
        rules_map[rule[0]].append(rule[1])
    valid_updates = []
    for update in updates:
        valid_update = True
        for i, page in enumerate(update):
            for next_page in update[i+1:]:
                if next_page not in rules_map[page]:
                    valid_update = False
                    break
            if not valid_update:
                break

        if valid_update:
            valid_updates.append(update)

    return sum(update[len(update)//2] for update in valid_updates)



    
def p2():
    lines = day_input.split('\n')
    answer = 0

    first_section = True
    after_rules = defaultdict(list)
    before_rules = defaultdict(list)
    updates: list[list[int]] = []
    for line in lines:
        if len(line) == 0:
            first_section = False
            continue

        if first_section:
            [left, right] = line.split("|")
            left = int(left)
            right = int(right)

            after_rules[left].append(right)
            before_rules[right].append(left)
        else:
            update = [int(i) for i in line.split(",")]
            updates.append(update)

    for update in updates:
        valid_update = True
        for i in range(len(update)):
            before = update[:i]
            after = update[i + 1 :]

            for b in before:
                if before_rules[b] and update[i] in before_rules[b]:
                    valid_update = False
                    break

            for a in after:
                if after_rules[update[i]] and a not in after_rules[update[i]]:
                    valid_update = False
                    break

            if not valid_update:
                break

        if not valid_update:
            new_update = []
            while update:
                curr = update.pop(0)
                if all(u in after_rules[curr] for u in update):
                    new_update.append(curr)
                else:
                    update.append(curr)

            answer += new_update[len(new_update) // 2]

    return answer


if __name__ == '__main__':
    print(p1())
    print(p2())

