import math
from numpy import array, split

def groupByElves(entry):
    elvesFood = entry.rsplit("""

""")
    arr = []

    for x in range(len(elvesFood)):
        print(elvesFood[x] + "-")
        values = elvesFood[x].split("\n")
        total = 0
        for x in values:
            total += float(x)
        arr.append(total)

    print("groupByElves")

    return arr