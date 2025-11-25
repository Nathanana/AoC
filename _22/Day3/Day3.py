from Shortcuts.all import *

inp = str_input(22, 3).split("\n")
total = [0, 0]

for i, sack in enumerate(inp):
    cpts = (sack[:len(sack)//2], sack[len(sack)//2:])
    for item in cpts[0]:
        if item in cpts[1]:
            break
    total[0] += abc.index(item) + 1
    if i % 3 == 0:
        for item in sack:
            if item in inp[i + 1] and item in inp[i + 2]:
                break
        total[1] += abc.index(item) + 1
    

printTotal(total)