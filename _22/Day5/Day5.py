from Shortcuts.all import *

stacks = [[] for _ in range(9)]
rows, moves = str_input(22, 5).split("\n\n")
for row in reversed(rows.split("\n")):
    for i, box in enumerate(row[1::4]):
        if box.strip().isalpha():
            stacks[i].append(box)
moves = [list(map(int, move.split(" ")[1::2])) for move in moves.split("\n")]
def cratemover(p1):
    ctacks = deepcopy(stacks)
    for move in moves:
        amt, boxfrom, boxto = move[0], move[1] - 1, move[2] - 1
        if p1:
            for _ in range(amt):
                ctacks[boxto].append(ctacks[boxfrom].pop())
        else:
            buffer = []
            for _ in range(amt):
                buffer.append(ctacks[boxfrom].pop())
            while buffer:
                ctacks[boxto].append(buffer.pop())
    result = ''
    for stack in ctacks:
        result += stack[-1]
    return result

total = [cratemover(True), cratemover(False)]

printTotal(total)