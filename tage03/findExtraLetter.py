def findExtra(entry):
    res = []
    for rucksack in entry:
        start = rucksack[0:int(len(rucksack) / 2)]
        end = rucksack[int(len(rucksack) / 2):int(len(rucksack))]

        for x in start:
            if x in end:
                res.append(x)
                break
    return res