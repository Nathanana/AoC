from Shortcuts.parse import *

inp = str_input(24, 4).split("\n")
lines = [line.strip() for line in inp]

value_map = {"X": 1, "M": 2, "A": 3, "S": 4}
grid = {}
totals = [0, 0]

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[(x, y)] = value_map[char]

def continue_XMAS(coord, direction, value):
    next_coord = (coord[0] + direction[0], coord[1] + direction[1])
    if value == 4:
        totals[0] += 1
    elif next_coord in grid and grid[next_coord] == value + 1:
        continue_XMAS(next_coord, direction, value + 1)

def find_XMAS(coord):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (dx, dy) != (0, 0):
                next_coord = (coord[0] + dx, coord[1] + dy)
                if next_coord in grid and grid[next_coord] == 2:
                    continue_XMAS(next_coord, (dx, dy), 2)

def check_diagonals(coord):
    diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    X = [grid[(coord[0] + dx, coord[1] + dy)] for dx, dy in diagonals if (coord[0] + dx, coord[1] + dy) in grid]

    if len(X) == 4 and X.count(2) == 2 and X.count(4) == 2 and X[1] != X[2]:
        totals[1] += 1

for coord, value in grid.items():
    if value == 1: find_XMAS(coord)
    if value == 3: check_diagonals(coord)

print(f"Part 1: {totals[0]}")
print(f"Part 2: {totals[1]}")