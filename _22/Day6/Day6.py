from Shortcuts.all import *

inp = str_input(22, 6)

def get_marker(length):
    for i in range(len(inp) - length):
        letters = set(c for c in inp[i:i+length])
        if len(letters) == length:
            return i + length

total = [get_marker(4), get_marker(14)]

printTotal(total)