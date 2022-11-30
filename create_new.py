import sys
from pathlib import Path
base_file = """
from typing import List
from collections import defaultdict, Counter
from queue import Queue
from math import inf
import bisect

\n""".lstrip()

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
            exit(1)

if site:
    file_path = Path(__file__).parent / site / f'{first}.py'
    if file_path.exists():
        print(f"{file_path} exists")
        exit(0)
    with file_path.open('w') as file:
        file.write(base_file)
    print(f'{file_path} Created')
else:
    print('Unknown site provided')
    exit(1)
