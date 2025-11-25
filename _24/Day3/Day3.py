import re
from Shortcuts.parse import *

mem = str_input(24, 3)
enable = r"do\(\)"
disable = r"don't\(\)"
pattern = r"mul\(\d+,\d+\)"

def solution(p2, string):
    if p2:
        valid = []
        dostrings = re.split(enable, string)
        for string in dostrings:
            dontstrings = re.split(disable, string)
            valid += re.findall(pattern, dontstrings[0])    
    else: 
        valid = re.findall(pattern, string)
    sum = 0    
    for mul in valid:
        mul = mul[4:-1].split(",")
        sum += int(mul[0]) * int(mul[1])
    return sum
    
print(f"Part 1: {solution(False, mem)}")
print(f"Part 1: {solution(True, mem)}")