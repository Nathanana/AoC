from Shortcuts.all import *

inp = [pair.split(" ") for pair in str_input(22, 2).split("\n")]
total = [0, 0]

opp, move = ["A", "B", "C"], ["X", "Y", "Z"]

for pair in inp:
    total[0] += (move.index(pair[1]) + 1) + ((move.index(pair[1]) - opp.index(pair[0]) + 1) % 3) * 3
    total[1] += (move.index(pair[1])) * 3 + (opp.index(pair[0]) - 1 + move.index(pair[1])) % 3 + 1
        
printTotal(total)