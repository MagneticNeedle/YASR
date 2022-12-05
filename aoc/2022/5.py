from  ..aoc import get_input


day_input = get_input(5).strip()
def print_stack(stack):
    for i in stack:
        print(*i)
    print()

stack_raw, movements = day_input.split('\n\n')
stack = []
stack_temp = []
stacks = 8
stack_raw = stack_raw.split('\n')[0:-1]

for i in range(1, len(stack_raw[0]), 4):
    stack.append([])
    for j in range(stacks):
        crate = stack_raw[j][i]
        if crate != ' ':
            stack[-1].append(crate)
    stack[-1] = stack[-1][::-1]

movements = [list(map(int, [j for j in  i.split(' ') if j.isnumeric()])) for i in movements.split('\n')]
for movement in movements:
    times,from_, to = movement[0], movement[1]-1, movement[2]-1
    
    temp_stack = []
    while times > 0 and stack[from_]:
        temp_stack.append(stack[from_].pop())
        times -= 1
    stack[to].extend(temp_stack[::-1])

print(''.join([i[-1] for i in stack if len(i)]))
