from Shortcuts.all import *

inp = [list(map(lambda x: list(map(int, x.split("-"))), pair.split(","))) for pair in str_input(22, 4).split("\n")]
total = [0, 0]
  
total[0] = sum((pair[0][0] - pair[1][0]) * (pair[0][1] - pair[1][1]) <= 0 for pair in inp)     
total[1] = sum(any(value in range(pair[1][0], pair[1][1] + 1) for value in range(pair[0][0], pair[0][1] + 1)) for pair in inp)
             
printTotal(total)