from numpy import array

def findThreeBiggest(arr: array):
    arr.sort()
    return arr[len(arr) - 1] + arr[len(arr) - 2] + arr[len(arr) - 3]