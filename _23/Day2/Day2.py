from Shortcuts.parse import *

inp = get_input(23, 2).split("\n")
inp = [[y.split() for y in x.split(";")] for x in inp]
total1 = 0
total2 = 0

for idx, x in enumerate(inp):
    p = True
    mred, mgreen, mblue = 0, 0, 0
    for bag in x:   
        red, green, blue = 0, 0, 0
        for n, w in enumerate(bag):
            if w.isdigit():
                if bag[n+1].startswith("red"):
                    red = int(w)
                if bag[n+1].startswith("green"):
                    green = int(w)
                if bag[n+1].startswith("blue"):
                    blue = int(w)
                if red > 12 or green > 13 or blue > 14:
                    p = False
                mred = max(mred, red)
                mgreen = max(mgreen, green)
                mblue = max(mblue, blue)
    total2 += mred*mgreen*mblue
    if p:
        total1 += idx+1
        
print(total1)
print(total2)