from Shortcuts.all import *

orders, updates = str_input(24, 5).split("\n\n")
orders = orders.split("\n")
updates = updates.split("\n")
total = [0, 0]
ordering = {}
rordering = {}

for pages in orders:
    pages = pages.split("|")
    if pages[0] not in ordering:
        ordering[pages[0]] = []
    ordering[pages[0]].append(pages[1])

for update in updates:
    update = update.split(",")
    valid = True
    for _ in range(1000):
        for i, page in enumerate(list(reversed(update))):
            for j, page2 in enumerate(list(reversed(update))[i + 1:]):
                if page in ordering and page2 in ordering[page]:
                    update.remove(page2)
                    update.insert(len(update) - i, page2)
                    valid = False
    if valid:
        total[0] += int(update[(len(update)//2)])
    else:
        total[1] += int(update[(len(update)//2)])
            
printTotal(total)