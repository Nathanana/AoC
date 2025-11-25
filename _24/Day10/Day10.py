from Shortcuts.all import *

inp = graph_input(24, 10)
starts = set()

for coord, obj in inp.items():
    if obj == 0:
        starts.add(coord)

def rate(p2): 
    rating = 0   
    for startcoord in starts:
        visited = set()
        start = inp[startcoord]
        stack = [(startcoord, start)]
        while stack:
            coord, obj = stack.pop()
            if not p2:
                visited.add((coord, obj))
            if obj == 9:
                rating += 1
                continue
            surr = check_coord(inp, coord, NESW)
            for (o_coord, o_obj) in surr:
                if o_obj == obj + 1 and (o_coord, o_obj) not in visited: 
                    stack.append((o_coord, o_obj))
    return rating

total = [rate(False), rate(True)]
            
printTotal(total)