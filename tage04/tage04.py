import entryTage04 as e

import splitPairs as sp

import checkRanges as cr

pairs = sp.splitPairs(e.entry)

result1 = cr.checkRanges(pairs)
print(result1)