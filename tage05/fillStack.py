import queue

def fillStack(entry):
    # reverse order to fill the stack later
    entry.reverse()

    # setting the stack at his empty state
    stacks = []
    for x in range(9):
        # initializing the stack with the max value would ever have
        stacks.append(queue.LifoQueue(maxsize=56))

    # filling up the stacks
    for row in entry:
        for i in range(9):
            value = row[4 * i + 1]
            if value != " ":
                stacks[i].put(value)
    return stacks