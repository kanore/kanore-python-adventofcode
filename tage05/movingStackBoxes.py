def movingStackBoxes(moves, stacks):
    for x in stacks:
        print(x.qsize())

    for x in moves:
        print(x)
        # getting the numbers for the moves
        __, amount, __, fromP, __, toP = x.split(" ")
        amount = int(amount) 
        fromP = int(fromP) - 1
        toP = int(toP) - 1

        # moving the boxes
        for i in range(amount):
            val = stacks[fromP].get()
            stacks[toP].put(val)

    for x in stacks:
        print(x.qsize())

    return stacks