def commonItems(entry):
    res = []

    for x in range(100):
        first = entry[3 * x]
        second = entry[(3 * x) + 1]
        third = entry[(3 * x) + 2]

        if len(first) < len(second) and len(first) < len(third):
            smallest = first
            ruck2 = second
            ruck3 = third

        elif len(second) < len(third):
            smallest = second
            ruck2 = first
            ruck3 = third

        else:
            smallest = third
            ruck2 = first
            ruck3 = second

        for y in smallest:
            if y in ruck2 and y in ruck3:
                res.append(y)
                break
            
    return res