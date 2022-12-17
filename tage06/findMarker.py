def findTopIndex(entry, markerSize):
    # max index it will check 
    # can't check beyond top because the maths won't fit
    top = len(entry) - markerSize + 1
    for i in range(top):
        # splitting every 'markerSize' sequence
        sequence = entry[i:i + markerSize]
        # checking if is a valid sequence
        if checkSequence(sequence, markerSize):
            return i + markerSize

def checkSequence(sequence, markerSize):
    for i in range(len(sequence)):
        # checking char if is in right side of the sequence
        if sequence[i] in sequence[i + 1:markerSize]:
            return False
    
    return True