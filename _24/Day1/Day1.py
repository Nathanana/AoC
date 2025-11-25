from collections import Counter
from Shortcuts.parse import *

lines = [list(map(int, line.strip().split('   '))) for line in str_input(24, 1).split("\n")]

listA, listB = zip(*lines)
difference = [abs(a - b) for a, b in zip(sorted(listA), sorted(listB))]

print(f"Part 1: {sum(difference)}")

counterB = Counter(listB)
similarity = sum(num * counterB[num] for num in listA)

print(f"Part 2: {similarity}")