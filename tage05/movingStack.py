import queue

def movingStackBoxes9000(moves, stacks):
    for x in moves:
        # getting the numbers for the moves
        __, amount, __, fromP, __, toP = x.split(" ")
        amount = int(amount) 
        fromP = int(fromP) - 1
        toP = int(toP) - 1

        # moving the boxes
        for i in range(amount):
            val = stacks[fromP].get()
            stacks[toP].put(val)
        break

    return stacks

def movingStackBoxes9001(moves, stacks):
    for x in stacks:
        print(x.qsize())

    tmp = queue.LifoQueue(maxsize=56)
    for x in moves:
        # getting the numbers for the moves
        __, amount, __, fromP, __, toP = x.split(" ")
        amount = int(amount) 
        fromP = int(fromP) - 1
        toP = int(toP) - 1

        # moving the boxes to a tmp stack
        for i in range(amount):
            v = stacks[fromP]
            val = v.get()
            tmp.put(val)

        # moving from the tmp to the stack
        for i in range(amount):
            stacks[toP].put(tmp.get())
        
        print("size",tmp.qsize())

    for x in stacks:
        print(x.qsize())

    return stacks