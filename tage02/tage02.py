
import entryTage02 as e

import splitRound as sr

import calculateTotal as ct

result1 = ct.calculateTotal(sr.splitRound(e.entry))

print("Day 02 part 1 result: ", result1)

import calculateTotal2 as ct2

result2 = ct2.calculateTotal2(sr.splitRound(e.entry))

print("Day 02 part 2 result: ", result2)