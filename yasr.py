#!.venv/bin/python3
import sys
from pathlib import Path

base_path = Path(__file__).parent

base_file = """
from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect

\n""".lstrip()


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
            base_file = base_file.strip()
            base_file += f"""\nfrom ..aoc_api import get_input\n\nday_input = get_input({first}).strip()\n\n"""
        case _:
            print("Unkown site, exiting....")
            exit(1)
file_path = Path(__file__).parent / site / f'{first}.py'
ensure_base_dir_exists(file_path.parent)

if not file_path.exists():
    file_path.write_text(base_file)
    print(f'{file_path} Created')
else:
    print(f'{file_path} Already exists')
