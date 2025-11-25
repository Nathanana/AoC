from functools import reduce
from Shortcuts.parse import str_input

inp = str_input(23, 5).split("\n\n")
seeds = [int(x) for x in inp[0].split()[1:]]

range_mappings = []
for block in inp[1:]:
    map_ranges = [y.split() for y in block.split("\n")[1:]]
    compiled_map = []
    for gs, ss, l in map_ranges:
        start, length = int(ss), int(l)
        gs = int(gs)
        compiled_map.append((start, start + length, gs))
    range_mappings.append(compiled_map)

def lookup(value):
    for mappings in range_mappings:
        for start, end, gs in mappings:
            if start <= value < end:
                value += (gs - start)
                break
    return value

print("Part 1:", min(map(lookup, seeds)))

def find_min_range(min_value, length, precision):
    step = max(1, precision // 10)
    best_seed = None
    best_value = float('inf')

    for seed in range(min_value, min_value + length, step):
        current_value = lookup(seed)
        if current_value < best_value:
            best_value = current_value
            best_seed = seed

    if precision > 1:
        return find_min_range(best_seed - length // 20, min(length // 10, min_value + length - best_seed + length // 20), step)

    return best_value

results = []
for i in range(0, len(seeds), 2):
    results.append(find_min_range(seeds[i], seeds[i + 1], 1000000))
print("Part 2:", min(results))
