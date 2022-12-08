from numpy import array

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