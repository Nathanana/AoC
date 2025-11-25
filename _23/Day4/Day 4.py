from Shortcuts.parse import *

t1 = 0


inp = str_input(23, 4).split("\n")
inp = [line.split('|') for line in inp]
inp = [[word.split() for word in parts] for parts in inp]

qty = [1 for _ in range(len(inp))]

for i, (win, card) in enumerate(inp):
    m = sum(num in card for num in win)
    v = 0 if m == 0 else 2 ** (m - 1)
    t1 += v
    for j in range(i + 1, m + i + 1):
        qty[j] += qty[i]

print(f"Part 1: {t1}")
print(f"Part 2: {sum(qty)}")