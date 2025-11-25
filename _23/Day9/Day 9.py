from Shortcuts.parse import *


inp = str_input(23, 9).split('\n')
inp = [[int(x) for x in line.split(' ')] for line in inp]

def get_next_number(lis):
    pattern = [lis[i] - lis[i - 1] for i in range(1, len(lis))]
    value = get_next_number(pattern) if any(x != 0 for x in pattern) else 0
    return lis[-1] + value

def get_previous_number(lis):
    pattern = [lis[i] - lis[i - 1] for i in range(1, len(lis))]
    value = get_previous_number(pattern) if any(x != 0 for x in pattern) else 0
    return lis[0] - value

print(sum(get_next_number(line) for line in inp))
print(sum(get_previous_number(line) for line in inp))