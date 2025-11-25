from Shortcuts.parse import *

inp = get_input(23, 3).split("\n")
total1 = 0
grid = {}
mem = {}
sym = {}

for r, row in enumerate(inp):
    for c, cell in enumerate(row):
        grid[(r, c)] = cell
        
for r in range(len(inp)):
    for c in range(len(inp[0])):
        if (r, c) not in mem and grid[(r, c)].isdigit():
            cterm = c
            num = ""
            while cterm < len(inp[0]) and grid[(r, cterm)].isdigit():
                num += grid[(r, cterm)]
                cterm += 1
                
            part = False
            for rsurr in [-1, 0, 1]:
                for csurr in range(c-1, cterm+1):
                    if 0 <= r + rsurr < len(inp) and 0 <= csurr < len(inp[0]):
                        if grid[(r + rsurr, csurr)].isdigit():
                            mem[(r, csurr)] = int(num)
                        elif grid[(r + rsurr, csurr)] != ".":
                            part = True
            if part:
                total1 += int(num)
                            
print(total1)

ans = 0
for r in range(len(inp)):
    for c in range(len(inp[0])):
        if grid[(r, c)] == "*":
            adj = set((mem[(r + dr, c + dc)] if (r + dr, c + dc) in mem else 1) for dr, dc in
                      [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
            if len(adj) == 3:
                adj = list(adj)
                ans += adj[0] * adj[1] * adj[2]
print(ans)

