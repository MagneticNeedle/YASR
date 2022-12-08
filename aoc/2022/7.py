from ..aoc import get_input
from pathlib import Path
from collections import defaultdict

day_input = get_input(7)
day_input = day_input.strip().split('\n')
path = Path()
size_map = defaultdict(int)
dir_map = defaultdict(list)
line = 0
while line < len(day_input):    
    out : list[str] = day_input[line].split(' ')

    match out[1]:
        case 'cd':
            path = (path / out[2]).resolve()
            if out[2] != '..':
                dir_map[str(path.parent)].append(str(path))
 
        case 'ls':
            tline = line+1
            while tline < len(day_input) and not day_input[tline].startswith('$'):         
                if (size := day_input[tline].split(' ')[0]).isnumeric():
                    size_map[str(path)] += int(size)  # add size of file to parent dir                
                tline += 1
            for parent in path.parents:
                size_map[str(parent)] += size_map[str(path)]  # add size of file to parent of parent dir
            line = tline - 1
    
    line += 1
print(sum([i for i in size_map.values() if i <= 100000]))  # p1
remaining = 70000000 - size_map['/']
print(min(i for i in size_map.values() if remaining + i >= 30000000))  #p2
        

            
