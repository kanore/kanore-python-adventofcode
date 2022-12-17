def findFourTopIndex(entry):
    top = len(entry) - 3
    # print("Top",top)
    for i in range(top):
        sequence = entry[i:i+4]
        # print(i,sequence)
        if checkSequence(sequence):
            return i + 4

def checkSequence(sequence):
    if sequence[0] not in sequence[1:4]:
        if sequence[1] not in sequence[2:4]:
            if sequence[2] != sequence[3]:
                return True

    return False