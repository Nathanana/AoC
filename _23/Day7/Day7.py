from Shortcuts.parse import *
from collections import Counter

sum = 0

def SortByHand(array):
    n = len(array)

    for i in range(n):

        already_sorted = True

        for j in range(n - i - 1):

            if (array[j])[0] > (array[j + 1])[0]:

                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:

            break

    return array

def b14to10(base14_number):
    base14_mapping = { 'J': 1, 'T': 10,'Q': 12, 'K': 13, 'A': 14}

    base10_number = 0
    power = 0

    for digit in reversed(base14_number):
        if digit in base14_mapping:
            base10_number += base14_mapping[digit] * (14 ** power)
        else:
            base10_number += int(digit) * (14 ** power)
        power += 1

    return base10_number

input = str_input(23, 7).split("\n")

Final = []

for line in input:
    
    val = 0
    cline = line.split(' ')
    fix = int(cline[1].replace("\n",""))
    cline[1]=fix
    cline.append(cline[0])

    c = Counter(cline[0]).most_common(3)
    cline[0]=b14to10(cline[0])

    if ((c[0])[1]) == 5:
        val += 1000000 ** 4

    elif ((c[0])[1]) == 4:

        if "J" in cline[2]:
            val += 1000000 ** 4
        else:
            val += 100000 ** 4

    elif ((c[0])[1]) == 3 and ((c[1])[1]) == 2:

        if "J" in cline[2]:
            val += 1000000 ** 4
        else:
            val += 10000 ** 4

    elif ((c[0])[1]) == 3:

        if "J" in cline[2]:
            val += 100000 ** 4
        else:
            val += 1000 ** 4

    elif ((c[0])[1]) == 2 and ((c[1])[1]) == 2:

        if ((c[2])[0]) == "J":
            val += 10000 ** 4
        elif "J" in cline[2]:
            val += 100000 ** 4
        else:
            val += 100 ** 4

    elif ((c[0])[1]) == 2:

        if "J" in cline[2]:
            val += 1000 ** 4
        else:
            val += 10 ** 4

    elif "J" in cline[2]:

        val += 10 ** 4

    else:

        val += 1

    cline[0] = cline[0]*val
    cline.append(val)
    Final.append(cline)

SortByHand(Final)

for x in Final:
    sum += x[1]*(Final.index(x)+1)

print(f"Part 2: {sum}")