import math
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
from itertools import cycle
import aoc_api
import networkx as nx

day_input = aoc_api.get_input(8).strip()
# print(day_input)


def parse_raw(raw: str):
    raw = raw.split('\n\n')
    return raw[0].strip(), {
        line[0:3]: (line[7:10], line[12:15])
        for line in raw[1].strip().splitlines()
    }


def p1():
    instruction, nodes = parse_raw(day_input)
    curr_node = 'AAA'
    node_to_find = 'ZZZ'
    steps = 0
    while curr_node != node_to_find:
        direction = 0 if instruction[
                             steps % len(instruction)
                             ] == 'L' else 1
        curr_node = nodes[curr_node][direction]
        steps += 1
    return steps


def p2():
    instruction, nodes = parse_raw(day_input)
    nodes_ending_with_a = [k for k in nodes.keys() if k[-1] == 'A']
    ways = []
    for node in nodes_ending_with_a:
        for index, direction in enumerate(cycle(instruction)):
            direction = 0 if direction == 'L' else 1
            node = nodes[node][direction]
            if node.endswith('Z'):
                ways.append(index+1)
                break
    return math.lcm(*ways)


def do_graph():
    nodes_data = parse_raw(day_input)[1]
    G = nx.DiGraph(
        bgcolor='gray10',
        fontcolor='white',
        fontsize="800pt",
        pad="10",
        label="--- Day 8: Haunted Wasteland ---",
        labelloc="t",
        labeljust="l",
        size="120",
    )
    for node, (left, right) in nodes_data.items():
        G.add_node(
            node,
            color='white', shape='circle',
            style='filled', fillcolor='#00C896', fontcolor='black', fontsize='30pt'
        )
        edge_common_kwargs = {
            'style': 'filled',
            'len': '5pt',
            'penwidth': 10
        }
        G.add_edge(node, left, color="#D27C6A", **edge_common_kwargs)
        G.add_edge(node, right, color="#915665", **edge_common_kwargs)

    A = nx.nx_agraph.to_agraph(G)
    A.write('../data/problem_8_graph.dot')
    for layout in ['neato', 'twopi']:
        print(f'generating {layout}')
        A.draw(f'../data/problem_8_graph_{layout}.png', format='png', prog=layout)


if __name__ == '__main__':
    print(p1())
    print(p2())
    # do_graph()

