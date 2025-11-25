from Shortcuts.all import *

inp = graph_input(24, 6)
grid = str_input(24, 6).split("\n")

total = [0, 0]
start = ()
marked = set()

for coord, obj in inp.items():
    if obj == "^":
        start = coord
        inp[coord] = "."
        break

reflect = {0: [1, 3], 1: [0, 2], 2: [3, 1], 3: [2, 0]}

def patrol(map, first_dir, first_coord, p2):
    stack = [(first_dir, first_coord)]
    repeat = set()
    
    while stack:
        dir, coord = stack.pop()
        
        if (coord, dir) in repeat:
            return 1
        
        if coord not in map:
            continue
        
        marked.add(coord) if not p2 else None
        repeat.add((coord, dir))

        newcoord = (coord[0] + NESW[dir][0], coord[1] + NESW[dir][1])
        if newcoord in map and map[newcoord] == "#":
            stack.append(((dir + 1) % 4, coord))
            continue
        stack.append((dir, newcoord))
        continue
    return 0 if p2 else marked
        
total[0] = len(patrol(inp, 0, start, False))

for (r, c) in marked:
    if (r, c) == start:
        continue
    mapc = inp.copy()
    mapc[(r, c)] = '#'
    total[1] += patrol(mapc, 0, start, True)

printTotal(total)