import functools
from Shortcuts.all import *


@functools.lru_cache(maxsize=None)
def num_arrangements(springs, groups, spring_index, group_index, current_block):
    if spring_index == len(springs):
        if group_index == len(groups) and current_block == 0:
            return 1
        elif group_index == len(groups) - 1 and current_block == groups[group_index]:
            return 1
        return 0
    total_arrange = 0
    current_spring = springs[spring_index]
    if current_spring == "?":
        if current_block == 0:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, 0)
        if group_index < len(groups) and groups[group_index] == current_block:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index + 1, 0)
        total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, current_block + 1)
    elif current_spring == ".":
        if current_block == 0:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, 0)
        elif group_index < len(groups) and groups[group_index] == current_block:
            total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index + 1, 0)
    else:
        total_arrange += num_arrangements(springs, groups, spring_index + 1, group_index, current_block + 1)
    return total_arrange


inp = str_input(23, 12).split("\n")
arrangements = []
total = [0, 0]
for line in inp:
    springs, groups = line.split()
    groups = tuple(map(int, groups.split(",")))
    part1 = num_arrangements(tuple(springs), groups, 0, 0, 0)
    expanded_springs = tuple("?".join(springs for _ in range(5)))
    expanded_groups = groups * 5
    part2 = num_arrangements(expanded_springs, expanded_groups, 0, 0, 0)

    arrangements.append((part1, part2))

total[0] = sum(a[0] for a in arrangements)
total[1] = sum(a[1] for a in arrangements)

print(f"Part 1: {total[0]}")
print(f"Part 2: {total[1]}")
