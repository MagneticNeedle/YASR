import json
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
import aoc_api

day_input = aoc_api.get_input(19).strip()
# print(day_input)


def parse_raw(raw: str):
    raw = raw.split('\n\n')
    workflows = {
        line.split('{')[0]: line.split('{')[1].replace('}', '').split(',')
        for line in raw[0].strip().splitlines()
    }
    parts = [
        {match[0]: int(match[1]) for match in re.findall(r'(\w)=(\d+)', line)}
        for line in raw[1].strip().splitlines()
    ]
    return workflows, parts
    

def p1():
    workflows, parts = parse_raw(day_input)
    accepted_parts = []
    for part in parts:
        workflow_ended = False
        current_workflow = workflows['in']
        # print(part)
        while not workflow_ended:
            # print(current_workflow)
            for step in current_workflow:
                # print(f"checking for {step}")
                if step == 'A':
                    accepted_parts.append(part)
                    workflow_ended = True
                    break
                elif step == 'R':
                    workflow_ended = True
                    break
                elif any([sign in step for sign in "<>"]):
                    category, sign, value, goto = re.findall(r'(\w+)([<>])(\d+):(\w+)', step)[0]
                    # print(category, sign, value, goto, part[category])
                    if eval(f"{part[category]}{sign}{value}"):
                        if goto == 'A':
                            workflow_ended = True
                            accepted_parts.append(part)
                        elif goto == 'R':
                            workflow_ended = True
                        else:
                            current_workflow = workflows[goto]
                        break
                else:
                    current_workflow = workflows[step]

    print(sum([sum(part.values()) for part in accepted_parts]), sep='\n')
    


infile = open("../data/2023_19.txt")


wf = {}
for rule in infile:
    rule = rule.strip()
    if len(rule) == 0:
        break

    name, rest = rule.split("{")
    steps = rest.split("}")[0]
    steps = steps.split(",")

    wf[name] = []
    for step in steps:
        if not ":" in step:
            wf[name].append(["", "ALWAYS", 0, step])
            break
        step, dest = step.split(":")
        p = step[0]
        op = step[1]
        v = int(step[2:])
        wf[name].append([p, op, v, dest])

all_range = frozenset(range(1,4001))

def poss(name, incoming):
    if name == "R":
        return 0
    if name == "A":
        return len(incoming["x"]) * len(incoming["m"]) * len(incoming["a"]) * len(incoming["s"])

    total = 0
    wff = wf[name]
    range_left = dict((k, set(v)) for (k, v) in incoming.items())
    for i in range(len(wff)):
        p, op, v, dest = wf[name][i]

        if op == "ALWAYS":
            total += poss(dest, range_left)
            break
        elif op == ">":
            rng = range(v+1, 4001)
        elif op == "<":
            rng = range(1, v)
        else:
            assert(False)

        sending = {}
        for sk, sv in range_left.items():
            if sk != p:
                sending[sk] = sv
            else:
                sending[sk] = set()
                for i in rng:
                    if i in sv:
                        sv.remove(i)
                        sending[sk].add(i)
        total += poss(dest, sending)

    return total


result = poss("in", {"x": all_range, "m": all_range, "a": all_range, "s": all_range})

print(result)


if __name__ == '__main__':
    print(p1())
    print(p2())

