#!.venv/bin/python3
import sys
from pathlib import Path

base_path = Path(__file__).parent

BASE_FILE = """
import re
from collections import defaultdict, Counter
from queue import Queue
from math import *
import bisect
""".strip()

AOC_TEMPLATE = """
import aoc_api

day_input = aoc_api.get_input(5).strip()
print(day_input)


def parse_raw():
    ...

    
def p1():
    ...

    
def p2():
    ...


print(p1())
print(p2())
"""


def ensure_base_dir_exists(directory: Path):
    directory.mkdir(parents=True, exist_ok=True)
    directory.joinpath('__init__.py').touch(exist_ok=True)


first = sys.argv[1]
second = None if len(sys.argv) <= 2 else sys.argv[2]
if not first.isnumeric():  # by default make a leetcode solution
    raise ValueError('First arg must be a question number')

site = None
if not second:
    site = "leetcode"
else:
    match second[0]:
        case 'h':
            site = "hackerrank"
        case 'l':
            site = "leetcode"
        case 'a':            
            with open(base_path / 'aoc' / 'year.txt') as year:
                site = "aoc/" + year.read().strip()
            BASE_FILE += AOC_TEMPLATE.format(day=first)
        case _:
            print("Unkown site, exiting....")
            exit(1)
file_path = Path(__file__).parent / site / f'{first}.py'
ensure_base_dir_exists(file_path.parent)

if not file_path.exists():
    file_path.write_text(BASE_FILE)
    print(f'{file_path} Created')
else:
    print(f'{file_path} Already exists')
