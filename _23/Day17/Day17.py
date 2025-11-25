from Shortcuts.all import *

inp = graph_input(23, 17)
width, height =  dimension(23, 17)

def run(p2):
    hp = [(0, (0, 0), 0, -1)]
    marked = set()
    while hp:
        steps, pos, straight, direction = heapq.heappop(hp)
        if pos == (height - 1, width - 1) and (not p2 or straight >= 4):
            return steps
        for i, (dr, dc) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
            if direction >= 0 and (dr, dc) == [(-1, 0), (1, 0), (0, -1), (0, 1)][direction]:
                continue
            if direction != -1 and p2:
                if straight < 4 and i != direction:
                    continue
                if straight >= 10 and i == direction:
                    continue
            new_num_straight = 1 if i != direction else straight + 1
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos not in inp:
                continue
            if p2 and (new_pos, new_num_straight, i) not in marked:
                marked.add((new_pos, new_num_straight, i))
                heapq.heappush(hp, (steps + inp[new_pos], new_pos, new_num_straight, i))
            elif new_pos not in marked and straight < 4:
                marked.add(new_pos)
                heapq.heappush(hp, (steps + inp[new_pos], new_pos, new_num_straight, i))

print("Part 1:", run(False))
print("Part 2:", run(True))