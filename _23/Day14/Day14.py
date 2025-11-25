from Shortcuts.all import *

inp = graph_input(23, 14)
total = [0, 0]

def shift_up(inp):
    for coord, obj in inp.items():
        if obj == "O":
            shift = (coord[0] - 1, coord[1])
            while shift[0] >= 0 and inp.get(shift, "#") == ".":
                inp[coord] = "."
                inp[shift] = "O"
                coord = shift
                shift = (coord[0] - 1, coord[1])
            
def count(inp):
    rocks = [100 - r for (r, c), obj in inp.items() if obj == "O"]
    return sum(rocks)

coord = shift_up(inp)
total[0] = count(inp)
        
printTotal(total)