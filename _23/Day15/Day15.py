from Shortcuts.all import *

def HASH(step):
    current = 0
    for char in step:
        current += ord(char)
        current *= 17
        current %= 256
    return current

def perform_action(step):
    if step[-2] == "=":
        step = step.split("=")
        box = HASH(step[0])
        if box not in boxes:
            boxes[box] = []
        for lens in boxes[box]:
            if lens[0] == step[0]:
                lens[1] = step[1]
                return
        boxes[box].append(step)
    else:
        step = step.split("-")
        box = HASH(step[0])
        if box not in boxes:
            return
        for lens in boxes[box]:
            if lens[0] == step[0]:
                boxes[box].remove(lens)

inp = str_input(23, 15).split(",")
total = [0, 0]

boxes = {}

for step in inp:
    num = HASH(step)
    total[0] += num
    perform_action(step)
    
for box, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        total[1] += (box + 1) * (i + 1) * int(lens[1])
    
printTotal(total)