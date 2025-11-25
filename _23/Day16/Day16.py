from Shortcuts.all import *

inp = graph_input(23, 16)
grid = str_input(23, 16).split("\n")
edges = [coord for coord in inp if coord[0] in (0, len(grid) - 1) or coord[1] in (0, len(grid[0]) - 1)]
total = [0, 0]


reflect = {0: [1, 3], 1: [0, 2], 2: [3, 1], 3: [2, 0]}

def energize(first_dir, first_coord):
    stack = [(first_dir, first_coord)]
    marked = set()
    repeat = set()
    
    while stack:
        dir, coord = stack.pop()
        
        if coord not in inp or (coord, dir) in repeat:
            continue
        
        marked.add(coord)
        repeat.add((coord, dir))
        
        char = inp[coord]
        if char in "/\\":
            new_dir = reflect[dir][0 if char == "/" else 1]
            newcoord = (coord[0] + NESW[new_dir][0], coord[1] + NESW[new_dir][1])
            stack.append((new_dir, newcoord))
            continue
        elif char in "|-":
            if (char == "|" and dir in (1, 3)) or (char == "-" and dir in (0, 2)):
                new_dirs = reflect[dir]
                coord1 = (coord[0] + NESW[new_dirs[0]][0], coord[1] + NESW[new_dirs[0]][1])
                coord2 = (coord[0] + NESW[new_dirs[1]][0], coord[1] + NESW[new_dirs[1]][1])
                stack.append((new_dirs[0], coord1))
                stack.append((new_dirs[1], coord2))
                continue
        newcoord = (coord[0] + NESW[dir][0], coord[1] + NESW[dir][1])
        stack.append((dir, newcoord))
        continue
    return len(marked)

def possible_directions(coord):
    dirs = []
    if coord[0] == 0:
        dirs.append(2)
    elif coord[0] == len(grid) - 1:
        dirs.append(0)
    if coord[1] == 0:
        dirs.append(1)
    elif coord[1] == len(grid[0]) - 1:
        dirs.append(3)
    return dirs

start_combos = [(direction, coord) for coord in edges for direction in possible_directions(coord)]
        
total[0] = energize(1, (0, 0))
total[1] = max(energize(direction, coord) for direction, coord in start_combos)

printTotal(total)