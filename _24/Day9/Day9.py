from Shortcuts.all import *

inp = str_input(24, 9)
total = [0, 0]

file_len = []
spaces = []
lengths = dict()
predisk = []
starts = []

for i, length in enumerate(inp):
    if i % 2 == 0:
        lengths[i//2] = int(length)
        starts.append(len(predisk))
        for j in range(int(length)):
            predisk.append(i//2)
    else:
        spaces.append([int(length), len(predisk)])
        for j in range(int(length)):
            predisk.append(-1)

def p1(disk):
    j = len(disk) - 1         
    for i, value in enumerate(disk):
        if j == i:
            break
        if value == -1:
            while disk[j] == -1:
                j -= 1
            disk[i], disk[j] = disk[j], disk[i]
    return checksum(disk)
            
def p2(disk):
    for id in range(len(lengths)-1, 0, -1):
        for i, (length, start) in enumerate(spaces):
            if start >= starts[id] or length < lengths[id]:
                continue
            for j in range(lengths[id]):
                disk[start + j] = id
                disk[starts[id] + j] = -1
            spaces[i][0] -= lengths[id]
            spaces[i][1] += lengths[id]
            break
    return checksum(disk)

def checksum(disk):
    csum = 0
    for i, value in enumerate(disk):
        if value != -1:
            csum += i * value
    return csum

total = [p1(predisk.copy()), p2(predisk.copy())]
    
printTotal(total)