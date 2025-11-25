from Shortcuts.all import *

inp = str_input(22, 1).split("\n\n")
total = [0, 0]

cals = [sum(map(int, elf.split("\n"))) for elf in inp]

total[0] = max(cals)
total[1] = sum(sorted(cals)[:3])

printTotal(total)