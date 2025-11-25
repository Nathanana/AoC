import functools
import math
from Shortcuts.parse import *

inp = str_input(23, 8).split("\n\n")

dir = [char for char in inp[0]]
inp = inp[1].split("\n")
mappings = {}
result = 0

for i, m in enumerate(inp):
    inp[i] = [x.strip("()").split(",") for x in m.replace(" ", "").split("=")]
    mappings[(inp[i][0][0])] = inp[i][1]
    
def PathFind(code):
    steps = 0
    while not code.endswith('Z'):
        code = mappings[code][0 if dir[steps % len(dir)] == 'L' else 1]
        steps += 1
    return steps
        
print(PathFind("AAA"))
print(functools.reduce(lambda a, b: a * b // math.gcd(a, b), [PathFind(x) for x in filter(lambda x: x.endswith('A'), mappings.keys())]))
