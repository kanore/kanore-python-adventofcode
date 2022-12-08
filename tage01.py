import math
from numpy import array, split

import entry

def groupByDeer(entry):
    deerFood = entry.rsplit("""

""")
    arr = []

    for x in range(len(deerFood)):
        print(deerFood[x] + "-")
        values = deerFood[x].split("\n")
        total = 0
        for x in values:
            total += float(x)
        arr.append(total)

    print("groupByDeer")

    return arr

def findBiggest(arr: array):
    value = 0
    index = -1
    savedIndex = -1
    print("findBiggest")
    for a in arr:
        print()
        index += 1
        if a > value:
            value = a
            savedIndex = index
    print(savedIndex)
    print(len(arr))
    return value

result1 = findBiggest(groupByDeer(entry.entry))

print("Day 01 result: ", result1)