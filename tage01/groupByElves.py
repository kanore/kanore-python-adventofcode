
def groupByElves(entry):
    elvesFood = entry.rsplit("""

""")
    arr = []

    for x in range(len(elvesFood)):
        values = elvesFood[x].split("\n")
        total = 0
        for x in values:
            total += float(x)
        arr.append(total)

    return arr