from Shortcuts.parse import *

lines = [list(map(int, line.strip().split())) for line in str_input(24, 2).split("\n")]

count = 0
countPt2 = 0

def checkIfValid(line):
    ascending = line == sorted(line) and all(1 <= (line[i + 1] - line[i]) <= 3 for i in range(len(line) - 1))
    descending = line == sorted(line, reverse=True) and all(1 <= (line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))
    return ascending or descending

for line in lines:
    if checkIfValid(line):
        count += 1
        continue

    for i in range(len(line)):
        if checkIfValid(line[:i] + line[i + 1:]):
            countPt2 += 1
            break
 
print(f"Part 1: {count}")
print(f"Part 2: {count + countPt2}")
