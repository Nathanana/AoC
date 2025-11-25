from Shortcuts.all import *

inp = graph_input(24, 8)
total = [0, 0]
antennas = {}
an1 = set()
an2 = set()

for coord, obj in inp.items():
    if obj != ".":
        antennas.setdefault(obj, []).append(coord)

for coords in antennas.values():
    for coord1, coord2 in it.permutations(coords, 2):  # Generate all ordered pairs
        dx, dy = coord1[0] - coord2[0], coord1[1] - coord2[1]
        step = 0
        while (x := coord1[0] + dx * step, y := coord1[1] + dy * step) in inp:
            an2.add((x, y))
            if step == 1:
                an1.add((x,y))
            step += 1
                
total[0], total[1] = len(an1), len(an2)

printTotal(total)