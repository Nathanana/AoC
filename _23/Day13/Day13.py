from Shortcuts.all import *

inp = str_input(23, 13).split("\n\n")

total = [0, 0]

def differences(str1, str2):
    if len(str1) != len(str2):
        return False

    diff_count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_count += 1

    return diff_count

def check_reflection(index, pattern, smudge=0, p2=False):
    if smudge > 1: return False
    distance = min(index, len(pattern) - index - 2)
    for r in range(1, distance + 1):
        smudge += differences(pattern[index - r], pattern[index + r + 1])
    if p2:
        return smudge == 1
    return smudge == 0

def scan(pattern, multi):
    for r in range(len(pattern)):
        if r < len(pattern) - 1:
            diff = differences(pattern[r], pattern[r + 1])
            if check_reflection(r, pattern, diff, False):
                total[0] += multi * (r + 1)
            elif check_reflection(r, pattern, diff, True):
                total[1] += multi * (r + 1)

for pattern in inp:
    pattern = [[piece for piece in line] for line in pattern.split("\n")]
    scan(pattern, 100)
    pattern = np.array(pattern).transpose().tolist()
    scan(pattern, 1)
                
print(f"Part 1: {total[0]}")
print(f"Part 2: {total[1]}")