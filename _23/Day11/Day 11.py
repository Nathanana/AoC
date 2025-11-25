from Shortcuts.all import *

grid = str_input(23, 11).split("\n")

total = [0, 0]
rows, cols = len(grid), len(grid[0])

galaxies = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == "#"]

rows_to_double = {r for r in range(rows) if all(grid[r][c] == '.' for c in range(cols))}
cols_to_double = {c for c in range(cols) if all(grid[r][c] == '.' for r in range(rows))}

for i, g1 in enumerate(galaxies):
    for g2 in galaxies[i + 1:]:
        xdist = x2dist = abs(g2[1] - g1[1])
        ydist = y2dist = abs(g2[0] - g1[0])
        startx = min(g2[1], g1[1])
        starty = min(g2[0], g1[0])
        for dx in range(1, xdist + 1):
            if startx + dx in cols_to_double:
                xdist += 1
                x2dist += 999999
        for dy in range(1, ydist + 1):
            if starty + dy in rows_to_double: 
                ydist += 1
                y2dist += 999999
        total[0] += (xdist + ydist)
        total[1] += (x2dist + y2dist)
        
print(f"Part 1: {total[0]}")
print(f"Part 2: {total[1]}")