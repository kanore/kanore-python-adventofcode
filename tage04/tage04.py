import entryTage04 as e

import splitPairs as sp

import checkFullOverlap as cfo

import checkPartOverlap as cpo

pairs = sp.splitPairs(e.entry)

result1 = cfo.checkFullOverlap(pairs)
print("Day 04 part 1 result: ", result1)

result2 = cpo.checkPartOverlap(pairs)
print("Day 04 part 2 result: ", result2)