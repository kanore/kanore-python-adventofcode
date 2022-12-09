from numpy import array

def findBiggest(arr: array):
    value = 0
    for a in arr:
        if a > value:
            value = a
    return value